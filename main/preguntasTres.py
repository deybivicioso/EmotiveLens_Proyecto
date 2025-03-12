import tkinter as tk
import subprocess
import sys
from pathlib import Path
from tkinter import messagebox

# Creación de la ventana principal
root = tk.Tk()
root.title("Encuesta de Satisfacción")
root.geometry("700x500")
root.configure(bg="#7A98B2")

# Variables para las respuestas
tipo_fuente = ("Arial", 12)
pregunta1_var, pregunta2_var, pregunta3_var = tk.StringVar(), tk.StringVar(), tk.StringVar()

# Obtener la carpeta principal del proyecto
project_root = Path(__file__).resolve().parent.parent  

# Función para validar respuestas antes de enviar
def validar_y_enviar():
    if not (pregunta1_var.get() and pregunta2_var.get() and pregunta3_var.get()):
        messagebox.showerror("Error", "Por favor, responde todas las preguntas antes de continuar.")
        return
    messagebox.showinfo("Encuesta enviada", "¡Gracias por completar la encuesta!")
    root.destroy()

# Función para regresar a la ventana anterior
def abrir_anterior():
    root.destroy()
    preguntas_dos_path = project_root / "main" / "preguntasDos.py"
    subprocess.run([sys.executable, str(preguntas_dos_path)])

# Función para crear preguntas con opciones de respuesta
def crear_pregunta(texto, variable, opciones):
    tk.Label(root, text=texto, bg="#7A98B2", font=tipo_fuente).pack(pady=10)
    frame = tk.Frame(root, bg="#7A98B2")
    frame.pack()
    for texto, valor in opciones:
        tk.Radiobutton(frame, text=texto, variable=variable, value=valor, bg="#7A98B2", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)

crear_pregunta("¿Cómo describiría la actitud del personal durante su atención?", pregunta1_var, [("Profesional y cordial", "Profesional y cordial"), ("Neutra", "Neutra"), ("Desinteresada", "Desinteresada")])
crear_pregunta("¿Se sintió escuchado y comprendido por el personal?", pregunta2_var, [("Sí, totalmente", "Sí, totalmente"), ("Solo en parte", "Solo en parte"), ("No, en absoluto", "No, en absoluto")])
crear_pregunta("¿El personal mostró conocimiento y experiencia en el servicio prestado?", pregunta3_var, [("Sí, demostraron gran conocimiento", "Sí, demostraron gran conocimiento"), ("Un conocimiento básico", "Un conocimiento básico"), ("No parecían tener experiencia", "No parecían tener experiencia")])

# Botones de navegación en el centro
frame_botones = tk.Frame(root, bg="#7A98B2")
frame_botones.pack(pady=20)

btn_atras = tk.Button(frame_botones, text="Atrás", command=abrir_anterior, bg="#FF6347", font=tipo_fuente)
btn_atras.pack(side=tk.LEFT, padx=20)

btn_enviar = tk.Button(frame_botones, text="Enviar Encuesta", command=validar_y_enviar, bg="#16CD7B", font=tipo_fuente)
btn_enviar.pack(side=tk.LEFT, padx=20)

# Mantener la ventana abierta
root.mainloop()