import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
from pathlib import Path

# Obtener la carpeta principal del proyecto
project_root = Path(__file__).resolve().parent.parent

# Función para validar las respuestas antes de avanzar
def validar_y_abrir_siguiente():
    nombre = entry_nombre.get().strip()
    correo = entry_correo.get().strip()
    telefono = entry_telefono.get().strip()
    
    if not (nombre and correo and telefono and pregunta1_var.get() and pregunta2_var.get() and pregunta3_var.get()):
        messagebox.showerror("Error", "Por favor, complete todos los campos antes de continuar.")
        return
    
    root.destroy()
    preguntas_dos_path = project_root / "main" / "preguntasDos.py"
    subprocess.run([sys.executable, str(preguntas_dos_path)])

# Creación de la ventana de preguntas
root = tk.Tk()
root.title("Encuesta de eficiencia de servicio")
root.geometry("500x500")
root.configure(bg="#7A98B2")

# Variables para las respuestas
tipo_fuente = ("Arial", 12)
pregunta1_var, pregunta2_var, pregunta3_var = tk.StringVar(), tk.StringVar(), tk.StringVar()

# Campos de entrada para los datos del usuario
def crear_label(texto):
    return tk.Label(root, text=texto, bg="#7A98B2", font=tipo_fuente)

def crear_entry():
    return tk.Entry(root, width=40)

label_nombre, entry_nombre = crear_label("Nombre:"), crear_entry()
label_correo, entry_correo = crear_label("Correo Electrónico:"), crear_entry()
label_telefono, entry_telefono = crear_label("Número de Teléfono:"), crear_entry()

for label, entry in [(label_nombre, entry_nombre), (label_correo, entry_correo), (label_telefono, entry_telefono)]:
    label.pack()
    entry.pack()

# Preguntas con opciones de respuesta
def crear_pregunta(texto, variable, opciones):
    tk.Label(root, text=texto, bg="#7A98B2", font=tipo_fuente).pack(pady=10)
    frame = tk.Frame(root, bg="#7A98B2")
    frame.pack()
    for texto, valor in opciones:
        tk.Radiobutton(frame, text=texto, variable=variable, value=valor, bg="#7A98B2", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)

crear_pregunta("¿Cómo calificarías la calidad general del servicio recibido?", pregunta1_var, [("Excelente", "Excelente"), ("Bueno", "Bueno"), ("Necesita mejorar", "Necesita mejorar")])
crear_pregunta("¿El tiempo de espera fue razonable?", pregunta2_var, [("Sí, fue rápido", "Sí, fue rápido"), ("Aceptable", "Aceptable"), ("Muy largo", "Muy largo")])
crear_pregunta("¿El personal fue amable y profesional?", pregunta3_var, [("Sí, muy amable y profesional", "Sí, muy amable y profesional"), ("Aceptable", "Aceptable"), ("No, no fue lo esperado", "No, no fue lo esperado")])

# Botón Siguiente
btn_siguiente = tk.Button(root, text="Siguiente", command=validar_y_abrir_siguiente, bg="#16CD7B", font=tipo_fuente)
btn_siguiente.pack(pady=20)

# Mantener la ventana abierta
root.mainloop()