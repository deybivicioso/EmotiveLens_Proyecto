import tkinter as tk
import subprocess
import sys
from pathlib import Path
import mysql.connector
import datetime

# Obtener la carpeta principal del proyecto
project_root = Path(__file__).resolve().parent.parent 

def guardar_seleccion(resumen, modo):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",          
            password="Deiinik6",  
            database="scanner"
        )
        cursor = conexion.cursor()

        for modo, timestamp in resumen.items():
            consulta = """
                INSERT INTO seleccion (timestamp, modo)
                VALUES (%s, %s)
            """
            valores = (timestamp, modo)
            cursor.execute(consulta, valores)

        cursor = conexion.cursor()
        conexion.commit()
        cursor.close()
        
    except mysql.connector.Error as err:
        print("Error al conectar con la base de datos:", err)


def guardar_modo_y_abrir(modo, ruta_script):
    resumen = {modo: datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    guardar_seleccion(resumen, modo)
    subprocess.run([sys.executable, str(ruta_script)])



def abrir_preguntas():
    """Cierra la ventana actual y abre preguntas.py."""
    root.destroy()  # Cierra la ventana actual
    preguntas_path = project_root / "main" / "preguntas.py"
    guardar_modo_y_abrir("Detallado", preguntas_path)  # Ejecuta preguntas.py

def abrir_scanner():
    """Cierra la ventana actual y abre scanner.py."""
    root.destroy() # Cierra la ventana actual
    scanner_path = project_root / "main" / "ejecutar_scanner.py"
    guardar_modo_y_abrir("Simple", scanner_path) # Ejecuta scanner.py
    

root = tk.Tk()
root.title("Seleccionar modo")
root.state("zoomed")
root.configure(bg="#7A98B2")

header = tk.Label(root, text="Selecciona el modo", font=("Arial", 14, "bold"), fg="white", bg="#7A98B2", width=50, height=2)
header.pack(pady=5)

frame = tk.Frame(root, bg="white")
frame.pack(pady=20)

CARD_WIDTH = 310
CARD_HEIGHT = 180

modes = [
    {"name": "Modo Detallado", "bio": "Encuesta detallada en base a preguntas", "command": abrir_preguntas},
    {"name": "Modo Simple", "bio": "Encuesta simple en base a escáner facial", "command": abrir_scanner}
]

for mode in modes:
    card = tk.Frame(frame, bg="#16CD7B", padx=10, pady=10, bd=2, relief="raised", width=CARD_WIDTH, height=CARD_HEIGHT)
    card.pack(pady=10)
    card.pack_propagate(False)

    name_label = tk.Label(card, text=mode["name"], font=("Arial", 14, "bold"), fg="white", bg="#16CD7B", wraplength=250)
    name_label.pack()

    bio_label = tk.Label(card, text=mode["bio"], font=("Arial", 10), wraplength=250, fg="white", bg="#16CD7B")
    bio_label.pack()

    # Agregar botón en ambos modos (Modo Detallado ejecuta función, Modo Simple no hace nada)
    button = tk.Button(card, text="Seleccionar", font=("Arial", 12, "bold"), bg="white", fg="#16CD7B", command=mode["command"])
    button.pack(pady=5)

root.mainloop()
