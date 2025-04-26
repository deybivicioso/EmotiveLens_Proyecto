import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
import mysql.connector
import subprocess
import sys



estilos_emociones = {
    "happy":    {"color": "#FFFACD", "emoji": "😀"},
    "sad":      {"color": "#ADD8E6", "emoji": "😟"},
    "angry":    {"color": "#F08080", "emoji": "😡"},
    "surprise": {"color": "#FFE4B5", "emoji": "😮"},
    "fear":     {"color": "#E6E6FA", "emoji": "😨"},
    "disgust":  {"color": "#E0FFFF", "emoji": "🤢"},
    "neutral":  {"color": "#F5F5F5", "emoji": "😐"},
}

def obtener_resultados():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Deiinik6",  # Cambia según tu configuración
            database="scanner"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT fecha_hora, emocion_predominante, cantidad, emocion_secundaria FROM resultados ORDER BY fecha_hora DESC")
        resultados = cursor.fetchall()
        conexion.close()
        return resultados
    except mysql.connector.Error as error:
        print("Error de conexión:", error)
        return []
    
def volver_app():
    subprocess.Popen([sys.executable, "app.py"])

def crear_historial_ui():
    ventana = tk.Tk()
    ventana.title("Historial")
    ventana.state("zoomed")
    ventana.configure(bg="white")

    # Barra superior
    barra = tk.Frame(ventana, bg="#7A9EB1", height=50)
    barra.pack(fill="x")
    btn_volver = tk.Button(barra, text="←", font=("Arial", 24, "bold"), bg= "#7A9EB1", fg="white", relief="flat", command=volver_app)
    btn_volver.pack(side="left", padx=10, pady=10)
    tk.Label(barra, text="HISTORIAL", font=("Arial", 14, "bold"), bg="#7A9EB1", fg="white", padx=20).pack(side="left", pady=10)

    # Contenedor con scroll
    contenedor_canvas = tk.Canvas(ventana, bg="white", highlightthickness=0)
    scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=contenedor_canvas.yview)
    contenedor_scroll = tk.Frame(contenedor_canvas, bg="white")

    contenedor_scroll.bind(
        "<Configure>",
        lambda e: contenedor_canvas.configure(scrollregion=contenedor_canvas.bbox("all"))
    )

    contenedor_canvas.create_window((0, 0), window=contenedor_scroll, anchor="nw")
    contenedor_canvas.configure(yscrollcommand=scrollbar.set)

    contenedor_canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Cargar datos de la BD
    datos = obtener_resultados()

    emociones_mostradas = set()

    for fecha_hora, emocion_predominante, cantidad, emocion_secundaria in datos:
        clave = (emocion_predominante.strip().lower(), emocion_secundaria.strip().lower())
        if clave in emociones_mostradas:
            continue
        emociones_mostradas.add(clave)


        emocion_clean = emocion_predominante.strip().lower()
        emocion_clean = emocion_clean.replace("ó", "o").replace("í", "i").replace("é", "e")
        estilo = estilos_emociones.get(emocion_clean)

        if estilo:
            color_fondo = estilo["color"]
            emoji = estilo["emoji"]
        else:
            print(f"Emoción no encontrada: '{emocion_clean}'")
            color_fondo = "#FFFFFF"
            emoji = "❓"
        

        frame = tk.Frame(contenedor_scroll, bg=color_fondo, bd=2, relief="solid")
        frame.pack(padx=20, pady=10, fill="x")

        # Subcontenedor
        interno = tk.Frame(frame, bg=color_fondo)
        interno.pack(fill="x", padx=400, pady=10)

        # Emoji o ícono a la izquierda
        tk.Label(interno, text= emoji, font=("Arial", 50), bg=color_fondo).pack(side="left", padx=10)

        # Info a la derecha
        info = tk.Frame(interno, bg=color_fondo)
        info.pack(side="left", fill="both", expand=False)

        tk.Label(info, text=f"Emocion Predominante: {emocion_predominante}", font=("Arial", 16, "bold"), bg=color_fondo).pack(anchor="w")
        tk.Label(info, text=f"emocion secundaria: {emocion_secundaria}         Cantidad: {cantidad}", font=("Arial", 12), bg=color_fondo).pack(anchor="w", pady=2)
        tk.Label(info, text=f"Fecha: {fecha_hora}", font=("Arial", 10, "italic"), bg=color_fondo, fg="gray").pack(anchor="w")

    ventana.mainloop()

crear_historial_ui()


    

