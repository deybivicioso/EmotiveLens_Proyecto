import tkinter as tk
import subprocess
import sys
from pathlib import Path

# Obtener la carpeta principal del proyecto
project_root = Path(__file__).resolve().parent.parent  

def abrir_preguntas():
    """Cierra la ventana actual y abre preguntas.py."""
    root.destroy()  # Cierra la ventana actual
    preguntas_path = project_root / "main" / "preguntas.py"
    subprocess.run([sys.executable, str(preguntas_path)])  # Ejecuta preguntas.py

root = tk.Tk()
root.title("Seleccionar modo")
root.geometry("400x500")
root.configure(bg="#7A98B2")

header = tk.Label(root, text="Selecciona el modo", font=("Arial", 14, "bold"), fg="white", bg="#7A98B2", width=50, height=2)
header.pack(pady=5)

frame = tk.Frame(root, bg="white")
frame.pack(pady=20)

CARD_WIDTH = 310
CARD_HEIGHT = 180

modes = [
    {"name": "Modo Detallado", "bio": "Encuesta detallada en base a preguntas", "command": abrir_preguntas},
    {"name": "Modo Simple", "bio": "Encuesta simple en base a escáner facial", "command": None}
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
