import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys
from pathlib import Path

# Obtener la carpeta principal del proyecto
project_root = Path(__file__).resolve().parent.parent  # Subir al directorio raíz del proyecto

print(f"Ruta del proyecto: {project_root}")

# Función de redirección de ventana
def redirect():
    root.destroy()
    app_path = project_root / "main" / "app.py"  # Ruta correcta para app.py
    subprocess.run([sys.executable, str(app_path)])  # Ejecutar app.py usando el intérprete actual

# Ventana principal
root = tk.Tk()
root.title("")
root.geometry("400x400")
root.configure(bg="white")

# Imagen
image_path = project_root / "assets" / "img" / "Emotive lens logo.png"  # Ruta correcta para la imagen
if image_path.exists():
    img = Image.open(image_path)
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
else:
    print(f"Error: La imagen no se encontró en {image_path}")
    img_tk = None

# Frame para animación
frame = tk.Frame(root, bg="white")
frame.pack(expand=True)

# Mostrar imagen si se cargó correctamente
if img_tk:
    label = tk.Label(frame, image=img_tk, bg="white")
else:
    label = tk.Label(frame, text="Imagen no encontrada", bg="white", fg="red")
label.pack()

# Animación y transición
def fade_in(alpha=0):
    if alpha <= 1:
        root.attributes('-alpha', alpha)
        root.after(50, fade_in, alpha + 0.10)
    else:
        root.after(2000, redirect)

# Inicio de animación
root.attributes('-alpha', 0)
fade_in()

# Ejecución
root.mainloop()
