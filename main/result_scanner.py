import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import subprocess
import sys
import mysql.connector
from datetime import datetime
from scanner import escaneo

project_root = Path(__file__).resolve().parent

EMOJIS = {
    "angry": "😡", "disgust": "🤢", "fear": "😨",
    "happy": "😀", "sad": "😟", "surprise": "😮", "neutral": "😐"
}

# Función para guardar resultados en la base de datos
def guardar_resultados_en_bd(resumen, emocion_predominante):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",          # <-- Reemplaza con tu usuario de MySQL
            password="Deiinik6",   # <-- Reemplaza con tu contraseña de MySQL
            database="scanner"
        )
        cursor = conexion.cursor()

        fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        emociones_ordenadas = sorted(resumen.items(), key=lambda x: x[1], reverse=True)

        top_emociones = emociones_ordenadas[:2]

        emocion_predominante = top_emociones[0][0] if len(top_emociones) > 0 else None
        emocion_secundaria = top_emociones[1][0] if len(top_emociones) > 1 else None 

        for emocion, cantidad in resumen.items():
            consulta = """
                INSERT INTO resultados (fecha_hora, emocion_predominante, cantidad, emocion_secundaria)
                VALUES (%s, %s, %s, %s)
            """
            valores = (fecha_hora_actual, emocion_predominante, cantidad, emocion_secundaria)
            cursor.execute(consulta, valores)

        conexion.commit()
        cursor.close()
        conexion.close()
        print("Resultados guardados correctamente.")

    except mysql.connector.Error as err:
        print(f"Error al conectar con la base de datos: {err}")

# Función principal para mostrar los resultados
def mostrar_resultados_con_grafico(detected_emotions):
    root = tk.Tk()
    root.title("Resultados del Escaneo Emocional")
    root.state("zoomed")

    top_bar = tk.Frame(root, bg="#7a98b2", height=50)
    top_bar.pack(fill="x")

    if detected_emotions:
        resumen = {}
        for emo in detected_emotions:
            resumen[emo] = resumen.get(emo, 0) + 1

        emocion_mayor = max(resumen, key=resumen.get)
        emoji_mayor = EMOJIS.get(emocion_mayor, "❓")

        # Guardar resultados en la base de datos
        guardar_resultados_en_bd(resumen, emocion_mayor)

        frame_contenido = tk.Frame(root, bg="white")
        frame_contenido.pack(expand=True, fill="both", padx=20, pady=20)

        frame_izquierda = tk.Frame(frame_contenido, bg="white")
        frame_izquierda.pack(side="right", expand=True, fill="both")

        frame_derecha = tk.Frame(frame_contenido, bg="white")
        frame_derecha.pack(side="right", expand=True, fill="both")

        labels = [f"{k} ({resumen[k]})" for k in resumen]
        sizes = [resumen[k] for k in resumen]
        colors = plt.cm.Set3(np.linspace(0, 1, len(labels)))

        fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
        ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140)
        ax.axis("equal")

        canvas = FigureCanvasTkAgg(fig, master=frame_izquierda)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True)

        etiqueta_emoji = tk.Label(frame_derecha, bg="white", text=emoji_mayor, font=("Arial", 300))
        etiqueta_emoji.pack(pady=(50, 10))

        etiqueta_texto = tk.Label(frame_derecha, text=f"Emoción predominante: {emocion_mayor.upper()}",
                                  font=("Arial", 16, "bold"), bg="white", fg="#333")
        etiqueta_texto.pack()

    else:
        label = tk.Label(root, text="No se detectaron emociones.", font=("Arial", 16))
        label.pack(pady=20)

    button_frame = tk.Frame(root, bg="white")
    button_frame.pack(pady=20)

    def open_barras():
        scanner_path = project_root / "barras.py"
        subprocess.run([sys.executable, str(scanner_path)])

    def create_round_button(parent, text, bg, fg, command=None, close_after=True):
        def on_click():
            if command:
                command()
            if close_after:
                root.destroy()
        button = tk.Button(parent, text=text, font=("Arial", 12, "bold"), bg=bg, fg=fg, padx=20, pady=10,
                           borderwidth=0, relief="flat", command=on_click)
        button.configure(width=20, height=2)
        return button

    button_cerrar = create_round_button(button_frame, "CERRAR", "#c53434", "white", root.destroy)
    button_cerrar.grid(row=0, column=0, padx=10)

    button_volver = create_round_button(button_frame, "VOLVER A ESCANEAR", "#16CD7B", "white",
                                        lambda: mostrar_resultados_con_grafico(escaneo()))
    button_volver.grid(row=0, column=1, padx=10)

    button_barras = create_round_button(button_frame, "VER GRAFICO DE BARRAS", "#16CD7B", "white", open_barras)
    button_barras.grid(row=0, column=2, padx=10)

    root.mainloop()
