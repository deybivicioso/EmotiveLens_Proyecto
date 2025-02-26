import tkinter as tk
from tkinter import messagebox

# Creación de la ventana principal
root = tk.Tk()
root.title("Encuesta de Satisfacción")
root.geometry("600x600")
root.configure(bg="#7A98B2")

# Variables para las respuestas
pregunta1_var = tk.StringVar()
pregunta2_var = tk.StringVar()
pregunta3_var = tk.StringVar()

def validar_respuestas():
    """Verifica que todas las preguntas estén respondidas antes de avanzar."""
    if not (pregunta1_var.get() and pregunta2_var.get() and pregunta3_var.get()):
        messagebox.showerror("Error", "Por favor, responde todas las preguntas antes de continuar.")
        return False
    return True

def avanzar():
    """Avanza a la siguiente ventana si las respuestas son válidas."""
    if validar_respuestas():
        root.withdraw()  # Oculta la ventana actual
        abrir_siguiente_ventana()

def retroceder():
    """Cierra la ventana actual y vuelve a la anterior."""
    root.quit()

def abrir_siguiente_ventana():
    """Crea la ventana siguiente."""
    ventana2 = tk.Toplevel()
    ventana2.title("Segunda Parte de la Encuesta")
    ventana2.geometry("600x600")
    ventana2.configure(bg="#7A98B2")

    tk.Label(ventana2, text="Gracias por completar la primera parte.", bg="#7A98B2", font=("Arial", 14)).pack(pady=20)

    tk.Button(ventana2, text="Cerrar", command=ventana2.quit, bg="#16CD7B", font=("Arial", 12)).pack(pady=20)

# Pregunta 1
label_pregunta1 = tk.Label(root, text="¿Cómo calificaría la disposición del personal para ayudarle?", bg="#7A98B2", font=("Arial", 12))
label_pregunta1.pack(pady=10)

frame_pregunta1 = tk.Frame(root, bg="#7A98B2")
frame_pregunta1.pack()

opciones_pregunta1 = [
    ("Muy dispuesto a ayudar", "Muy dispuesto"),
    ("Regular, solo respondieron cuando pregunté", "Regular"),
    ("Poco dispuesto a ayudar", "Poco dispuesto")
]

for texto, valor in opciones_pregunta1:
    tk.Radiobutton(frame_pregunta1, text=texto, variable=pregunta1_var, value=valor, bg="#7A98B2", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)

# Pregunta 2
label_pregunta2 = tk.Label(root, text="¿La solución brindada por el personal cumplió con sus expectativas?", bg="#7A98B2", font=("Arial", 12))
label_pregunta2.pack(pady=10)

frame_pregunta2 = tk.Frame(root, bg="#7A98B2")
frame_pregunta2.pack()

opciones_pregunta2 = [
    ("Sí, completamente", "Sí"),
    ("Parcialmente", "Parcialmente"),
    ("No, no resolvió mi problema", "No")
]

for texto, valor in opciones_pregunta2:
    tk.Radiobutton(frame_pregunta2, text=texto, variable=pregunta2_var, value=valor, bg="#7A98B2", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)

# Pregunta 3
label_pregunta3 = tk.Label(root, text="¿Qué tan claro fue el personal al explicarle los procedimientos o servicios?", bg="#7A98B2", font=("Arial", 12))
label_pregunta3.pack(pady=10)

frame_pregunta3 = tk.Frame(root, bg="#7A98B2")
frame_pregunta3.pack()

opciones_pregunta3 = [
    ("Muy claro", "Muy claro"),
    ("Algo confuso", "Algo confuso"),
    ("Nada claro", "Nada claro")
]

for texto, valor in opciones_pregunta3:
    tk.Radiobutton(frame_pregunta3, text=texto, variable=pregunta3_var, value=valor, bg="#7A98B2", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)

# Botones de navegación
frame_botones = tk.Frame(root, bg="#7A98B2")
frame_botones.pack(pady=20)

btn_atras = tk.Button(frame_botones, text="Atrás", command=retroceder, bg="#FF6347", font=("Arial", 12))
btn_atras.pack(side=tk.LEFT, padx=10)

btn_siguiente = tk.Button(frame_botones, text="Siguiente", command=avanzar, bg="#16CD7B", font=("Arial", 12))
btn_siguiente.pack(side=tk.LEFT, padx=10)

# Mantener la ventana abierta
root.mainloop()
