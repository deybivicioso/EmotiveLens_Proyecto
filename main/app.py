import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys
from pathlib import Path

# Obtener la carpeta principal del proyecto
project_root = Path(__file__).resolve().parent.parent  # Subir al directorio raíz del proyecto

# Creación de la ventana
root = tk.Tk()
root.title("Inicio")
root.geometry("400x500")
root.configure(bg="white")
root.attributes('-alpha', 0)

# Barra superior
top_bar = tk.Frame(root, bg="#7a98b2", height=50)
top_bar.pack(fill="x")

# Mostrar el logo
image_path = project_root / "assets" / "img" / "Emotive lens logo.png"  # Ruta correcta para la imagen
if image_path.exists():
    image = Image.open(image_path)
    image = image.resize((300, 300), Image.Resampling.LANCZOS)
    logo = ImageTk.PhotoImage(image)
else:
    print(f"Error: La imagen no se encontró en {image_path}")
    logo = None

# Frame para animación 
frame = tk.Frame(root, bg="white")
frame.pack(expand=True)

# Mostrar logo si se cargó correctamente
if logo:
    logo_label = tk.Label(root, image=logo, bg="white")
    logo_label.pack(pady=5)

# Animación entrada y salida
def fade_in(alpha=0):
    if alpha <= 1:
        root.attributes('-alpha', alpha)
        root.after(50, fade_in, alpha + 0.10)

def open_acercade():
    acercade_path = project_root / "main" / "acercade.py"  # Ruta correcta para acercade.py
    subprocess.run([sys.executable, str(acercade_path)])

# Inicio de animación 
fade_in()

# Marco de botones
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)

# Botones
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

    return button

# Crear botones
about_button = create_round_button(button_frame, text="ACERCA DE", bg="#c53434", fg="white", command=open_acercade)
survey_button = create_round_button(button_frame, text="INICIAR ENCUESTA", bg="#16cd7b", fg="white")

about_button.pack(side="left", padx=40, pady=100)
survey_button.pack(side="right", padx=40, pady=100)

# Ejecutar la app
root.mainloop()
