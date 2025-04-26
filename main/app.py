import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pygrabber.dshow_graph import FilterGraph
import subprocess
import sys
from pathlib import Path

  # Obtener la carpeta principal del proyecto
project_root = Path(__file__).resolve().parent.parent  # Subir al directorio raíz del proyecto

# Función para obtener la lista de cámaras disponibles con sus nombres
def get_camera_list():
    graph = FilterGraph()
    return graph.get_input_devices()  # Retorna una lista con los nombres de las cámaras

# Función para alternar entre modo oscuro y claro
dark_mode = False  
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

# Aplicar tema oscuro o claro
def apply_theme():
    if dark_mode:
        root.configure(bg="#2E2E2E")
        top_bar.configure(bg="#1C1C1C")
        settings_menu_button.configure(bg="#444", fg="white")
    else:
        root.configure(bg="white") 
        top_bar.configure(bg="#7a98b2")
        settings_menu_button.configure(bg="#ccc", fg="black")

# Creación de la ventana
root = tk.Tk()
root.title("Inicio")
root.state("zoomed")
root.configure(bg="white")
root.attributes('-alpha', 0)

dark_mode = False  # Estado inicial del tema

# Barra superior
top_bar = tk.Frame(root, bg="#7A98B2", height=50)
top_bar.pack(fill="x")

def open_settings():
    config_window = tk.Toplevel()
    config_window.title("Menu")
    config_window.geometry("400x300")

    tk.Label(config_window, text="Modo:").pack(pady=5)
    theme_button = tk.Button(config_window, text="Alternar Modo", command=toggle_theme)
    theme_button.pack(pady=5)

    tk.Label(config_window, text="Seleccionar Cámara:").pack(pady=5)
    camera_var = tk.StringVar()
    camera_list = get_camera_list()

    if camera_list:
        camera_dropdown = ttk.Combobox(config_window, textvariable=camera_var, values=camera_list, state="readonly")
        camera_dropdown.pack(pady=5)
        camera_dropdown.current(0)
    else:
        tk.Label(config_window, text="No se encontraron cámaras").pack()

def open_historial_resultados():
    root.destroy()
    historial_path = project_root / "main" / "historial_resultados.py"
    subprocess.run([sys.executable, str(historial_path)])

def open_historial_seleccion():
    root.destroy()
    historial_path = project_root / "main" / "historial_seleccion.py"
    subprocess.run([sys.executable, str(historial_path)])

# Panel desplegable de configuración
settings_menu_button = tk.Menubutton(top_bar, text="Menu", font=("Arial", 16), bg="#7A98B2", fg="white", relief="flat")
settings_menu_button.pack(side="left", padx=5, pady=5)

settings_menu = tk.Menu(settings_menu_button, tearoff=0)
settings_menu.add_command(label="Ajustes de cámara y tema", command=open_settings)
settings_menu.add_command(label="Historial de Resultados", command=open_historial_resultados)
settings_menu.add_command(label="Historial de Seleccion", command=open_historial_seleccion)
settings_menu_button.config(menu=settings_menu)



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
    root.destroy()
    acercade_path = project_root / "main" / "acercade.py"  # Ruta correcta para acercade.py
    subprocess.run([sys.executable, str(acercade_path)])

def open_iniciarencuesta():
    root.destroy()
    iniciarencuesta_path = project_root / "main" / "seleccion.py" # Ruta correcta para seleccion.py
    subprocess.run([sys.executable, str(iniciarencuesta_path)])

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
survey_button = create_round_button(button_frame, text="INICIAR ENCUESTA", bg="#16cd7b", fg="white", command=open_iniciarencuesta)


about_button.pack(side="left", padx=200, pady=100)
survey_button.pack(side="right", padx=200, pady=100)

#Ejecutar la app
root.mainloop()