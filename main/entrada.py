import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys

#Funcion de redireccion de ventana
def redirect():
    root.destroy()
    subprocess.run([sys.executable, "main/app.py"])



#Ventana principal
root = tk.Tk()
root.title("")
root.geometry("400x400")
root.configure(bg="white")

#Imagen
image_path = "assets/img/Emotive lens logo.png"
img = Image.open(image_path)
img = img.resize((200, 200))
img_tk = ImageTk.PhotoImage(img)

#frame para animacion 
frame = tk.Frame(root, bg="white")
frame.pack(expand=True)

#Mostrar imagen
label = tk.Label(frame, image=img_tk, bg="white")
label.pack()

#animacion y transicion 
def fade_in(alpha=0):
    if alpha <= 1:
        root.attributes('-alpha', alpha)
        root.after(50, fade_in, alpha + 0.10)
    else:
        root.after(2000, redirect)



#Inicio de animacion 
root.attributes('-alpha', 0)
fade_in()

#Ejecuccion
root.mainloop() 


