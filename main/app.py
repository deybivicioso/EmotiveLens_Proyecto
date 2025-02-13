import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys

#Creacion de la ventana
root = tk.Tk()
root.title("Inicio")
root.geometry("400x500")
root.configure(bg="white")
root.attributes ('-alpha', 0)

#Barra superior
top_bar = tk.Frame(root, bg="#7a98b2", height=50)
top_bar.pack(fill="x")

#Mostrar el logo
image_path = "assets/img/Emotive lens logo.png"
image = Image.open(image_path)
image = image.resize((300, 300), Image.Resampling.LANCZOS)
logo = ImageTk.PhotoImage(image)

#frame para animacion 
frame = tk.Frame(root, bg="white")
frame.pack(expand=True)

logo_label = tk.Label(root, image=logo, bg="white")
logo_label.pack(pady=5)

#Animacion entrada y salida
def fade_in(alpha=0):
    if alpha <=1:
        root.attributes('-alpha', alpha)
        root.after(50, fade_in, alpha + 0.10)
    
def open_acercade():
    subprocess.run([sys.executable, "main/acercade.py"])

#Inicio de animacion 
fade_in()

#marco de botones
button_frame = tk.Frame(root, bg="white")

#Botones
def create_round_button(parent, text, bg, fg, command=None):
    button = tk.Button(parent, text=text, font=("Arial", 12, "bold"), bg=bg, fg=fg, padx=20, pady=10,
                       borderwidth=0, relief="flat", command=command)
    button.configure(width=20, height=2)
    button.pack(side="left", padx=20)

    def on_enter(e):
        button.config(bg="#ffffff", fg=bg)

    def on_leave(e):
        button.config(bg=bg, fg=fg)

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    button.pack(side="left", padx=10)
    return button

button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)
about_button = create_round_button(button_frame, text="ACERCA DE", bg="#c53434", fg="white", command= open_acercade)
survey_button = create_round_button(button_frame, text="INICIAR ENCUESTA", bg="#16cd7b", fg="white")



about_button.pack(side="left", padx=200, pady=100)
survey_button.pack(side="right", padx=200, pady=100)

#Ejecutar la app
root.mainloop()