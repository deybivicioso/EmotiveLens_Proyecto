import tkinter as tk 
from tkinter import messagebox 

# Creación de la ventana de preguntas
root = tk.Tk()
root.title("Encuesta de eficiencia de servicio")
root.geometry("400x400")
root.configure(bg="#7A98B2")

# Preguntas de la encuesta de satisfacción: 
# Variables para las respuestas de las preguntas
pregunta1_var = tk.StringVar()
pregunta2_var = tk.StringVar()
pregunta3_var = tk.StringVar()

# El usuario ingresa sus datos: 
def guardar_respuestas():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    telefono = entry_telefono.get()
    
    # Verificar que todos los campos están completos
    if not nombre or not correo or not telefono:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return
    
    respuestas = {
        "nombre": nombre,
        "correo": correo,
        "telefono": telefono,
        "respuestas_preguntas": [pregunta1_var.get(), pregunta2_var.get(), pregunta3_var.get()]
    }
    
    # Aquí podrías guardar las respuestas en una base de datos o archivo
    print(respuestas)
    messagebox.showinfo("Gracias", "Gracias por completar la encuesta")
    root.quit()  # Cerrar la ventana

# Campos de entrada para los datos del usuario: 
label_nombre = tk.Label(root, text="Nombre:", bg="#7A98B2", font=("Arial", 12))
label_nombre.pack()
entry_nombre = tk.Entry(root, width=40)
entry_nombre.pack()

label_correo = tk.Label(root, text="Correo Electrónico:", bg="#7A98B2", font=("Arial", 12))
label_correo.pack()
entry_correo = tk.Entry(root, width=40)
entry_correo.pack()

label_telefono = tk.Label(root, text="Número de Teléfono:", bg="#7A98B2", font=("Arial", 12))
label_telefono.pack()
entry_telefono = tk.Entry(root, width=40)
entry_telefono.pack()

# Pregunta 1
label_pregunta1 = tk.Label(root, text="¿Cómo calificarías la calidad general del servicio recibido?", bg="#7A98B2", font=("Arial", 12))
label_pregunta1.pack(pady=15)

frame_pregunta1 = tk.Frame(root, bg="#7A98B2")
frame_pregunta1.pack()

opcion1_pregunta1 = tk.Radiobutton(frame_pregunta1, text="Excelente", variable=pregunta1_var, value="Excelente", bg="#7A98B2", font=("Arial", 10))
opcion1_pregunta1.pack(side=tk.LEFT)

opcion2_pregunta1 = tk.Radiobutton(frame_pregunta1, text="Bueno", variable=pregunta1_var, value="Bueno", bg="#7A98B2", font=("Arial", 10))
opcion2_pregunta1.pack(side=tk.LEFT)

opcion3_pregunta1 = tk.Radiobutton(frame_pregunta1, text="Necesita mejorar", variable=pregunta1_var, value="Necesita mejorar", bg="#7A98B2", font=("Arial", 10))
opcion3_pregunta1.pack(side=tk.LEFT)

# Pregunta 2
label_pregunta2 = tk.Label(root, text="¿El tiempo de espera fue razonable?", bg="#7A98B2", font=("Arial", 12))
label_pregunta2.pack(pady=10)

frame_pregunta2 = tk.Frame(root, bg="#7A98B2")
frame_pregunta2.pack()

opcion1_pregunta2 = tk.Radiobutton(frame_pregunta2, text="Sí, fue rápido", variable=pregunta2_var, value="Sí, fue rápido", bg="#7A98B2", font=("Arial", 10))
opcion1_pregunta2.pack(side=tk.LEFT)

opcion2_pregunta2 = tk.Radiobutton(frame_pregunta2, text="Aceptable", variable=pregunta2_var, value="Aceptable", bg="#7A98B2", font=("Arial", 10))
opcion2_pregunta2.pack(side=tk.LEFT)

opcion3_pregunta2 = tk.Radiobutton(frame_pregunta2, text="Muy largo", variable=pregunta2_var, value="Muy largo", bg="#7A98B2", font=("Arial", 10))
opcion3_pregunta2.pack(side=tk.LEFT)

# Pregunta 3
label_pregunta3 = tk.Label(root, text="¿El personal fue amable y profesional?", bg="#7A98B2", font=("Arial", 12))
label_pregunta3.pack(pady=10)

frame_pregunta3 = tk.Frame(root, bg="#7A98B2")
frame_pregunta3.pack()

opcion1_pregunta3 = tk.Radiobutton(frame_pregunta3, text="Sí, muy amable y profesional", variable=pregunta3_var, value="Sí, muy amable y profesional", bg="#7A98B2", font=("Arial", 10))
opcion1_pregunta3.pack(side=tk.LEFT)

opcion2_pregunta3 = tk.Radiobutton(frame_pregunta3, text="Aceptable", variable=pregunta3_var, value="Aceptable", bg="#7A98B2", font=("Arial", 10))
opcion2_pregunta3.pack(side=tk.LEFT)

opcion3_pregunta3 = tk.Radiobutton(frame_pregunta3, text="No, no fue lo esperado", variable=pregunta3_var, value="No, no fue lo esperado", bg="#7A98B2", font=("Arial", 10))
opcion3_pregunta3.pack(side=tk.LEFT)

# Botón de guardar la aplicación
boton_enviar = tk.Button(root, text="Enviar Encuesta", command=guardar_respuestas, bg="#16CD7B", font=("Arial", 12))
boton_enviar.pack()

# Mantener la ventana abierta
root.mainloop()