import tkinter as tk
from tkinter import messagebox

def seleccionar_modo(modo):
    messagebox.showinfo("Modo Seleccionado", f"Has seleccionado:{modo}")

root = tk.Tk()
root.title("Seleccionar modo")
root.geometry("400x500")
root.configure(bg="#7A98B2")


header = tk.Label(root, text="Selecciona el modo", font=("Arial", 14, "bold"), fg="#7A98B2", width=50, height=2)
header.pack(pady=5)

frame = tk.Frame(root, bg="white")
frame.pack(pady=20)

box_style = {"bg": "#7A98B2", "width": 25, "height": 5, "relief": "solid", "bd": 2}

developers = [
    {
        "name": "Modo Detallado",
        "bio": "Encuesta detallada en base a preguntas",
    },
    {
        "name": "Modo Simple",
        "bio": "Encuesta Simple en base a escaner facial",
    },
]


frame = tk.Frame(root, bg="#7A98B2")
frame.pack()

# Ajustes de tamaño de las tarjetas
CARD_WIDTH = 310  
CARD_HEIGHT = 180  


# Cargar datos en la interfaz en filas de 2
for i in range(0, len(developers), 2):
    row_frame = tk.Frame(frame, bg="#7A98B2")  
    row_frame.pack(pady=10)  

    for j in range(2):
        if i + j < len(developers):
            dev = developers[i + j]

            card = tk.Frame(row_frame, bg="#16CD7B", padx=10, pady=10, bd=2, relief="raised", width=CARD_WIDTH, height=CARD_HEIGHT)
            card.pack(side="left", padx=15) 
            card.pack_propagate(False) 

            name_label = tk.Label(card, text=dev["name"], font=("Arial", 14, "bold"), fg="white", bg="#16CD7B", wraplength=250)
            name_label.pack()

            bio_label = tk.Label(card, text=dev["bio"], font=("Arial", 10), wraplength=250, fg="white", bg="#16CD7B")
            bio_label.pack()



def create_round_button(parent, text, bg, fg):
    button = tk.Button(parent, text=text, font=("Arial", 12, "bold"), bg=bg, fg=fg, padx=20, pady=10,
                       borderwidth=0, relief="flat")
    button.configure(width=10, height=2)
    button.pack(side="left", padx=10)

    def on_enter(e):
        button.config(bg="#ffffff", fg=bg)

    def on_leave(e):
        button.config(bg=bg, fg=fg)

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    return button

frame = tk.Frame(root, bg="#7A98B2")
frame.pack(pady=20)

# Crear botones
btn_d = create_round_button(frame, text="SELECCIONAR", bg="#16cd7b", fg="white")
btn_s = create_round_button(frame, text="SELECCIONAR", bg="#16cd7b", fg="white")


btn_d.pack(side="left", padx=100, pady=10)
btn_s.pack(side="right", padx=100, pady=10)

#Ejecuccion
root.mainloop()