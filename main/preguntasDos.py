import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
from pathlib import Path

# Obtener la carpeta principal del proyecto
project_root = Path(__file__).resolve().parent.parent

# Función para validar respuestas antes de avanzar
def validar_y_abrir_siguiente():
    if not (pregunta1_var.get() and pregunta2_var.get() and pregunta3_var.get()):
        messagebox.showerror("Error", "Por favor, responde todas las preguntas antes de continuar.")
        return
    
    root.destroy()
    preguntas_tres_path = project_root / "main" / "preguntasTres.py"
    subprocess.run([sys.executable, str(preguntas_tres_path)])

# Función para regresar a la ventana anterior
def abrir_anterior():
    root.destroy()
    preguntas_path = project_root / "main" / "preguntas.py"
    subprocess.run([sys.executable, str(preguntas_path)])

# Creación de la ventana principal
root = tk.Tk()
root.title("Encuesta de Satisfacción")
root.geometry("700x500")
root.configure(bg="#7A98B2")

# Variables para las respuestas
tipo_fuente = ("Arial", 12)
pregunta1_var, pregunta2_var, pregunta3_var = tk.StringVar(), tk.StringVar(), tk.StringVar()

# Función para crear preguntas con opciones de respuesta
def crear_pregunta(texto, variable, opciones):
    tk.Label(root, text=texto, bg="#7A98B2", font=tipo_fuente).pack(pady=10)
    frame = tk.Frame(root, bg="#7A98B2")
    frame.pack()
    for texto, valor in opciones:
        tk.Radiobutton(frame, text=texto, variable=variable, value=valor, bg="#7A98B2", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)

crear_pregunta("¿Cómo calificaría la disposición del personal para ayudarle?", pregunta1_var, [("Muy dispuesto a ayudar", "Muy dispuesto"), ("Regular, solo respondieron cuando pregunté", "Regular"), ("Poco dispuesto a ayudar", "Poco dispuesto")])
crear_pregunta("¿La solución brindada por el personal cumplió con sus expectativas?", pregunta2_var, [("Sí, completamente", "Sí"), ("Parcialmente", "Parcialmente"), ("No, no resolvió mi problema", "No")])
crear_pregunta("¿Qué tan claro fue el personal al explicarle los procedimientos o servicios?", pregunta3_var, [("Muy claro", "Muy claro"), ("Algo confuso", "Algo confuso"), ("Nada claro", "Nada claro")])

# Botones de navegación
frame_botones = tk.Frame(root, bg="#7A98B2")
frame_botones.pack(pady=20)

btn_atras = tk.Button(frame_botones, text="Atrás", command=abrir_anterior, bg="#FF6347", font=tipo_fuente)
btn_atras.pack(side=tk.LEFT, padx=50)

btn_siguiente = tk.Button(frame_botones, text="Siguiente", command=validar_y_abrir_siguiente, bg="#16CD7B", font=tipo_fuente)
btn_siguiente.pack(side=tk.LEFT, padx=50)

# Mantener la ventana abierta
root.mainloop()
