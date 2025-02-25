import tkinter as tk
from PIL import Image, ImageTk  


developers = [
    {
        "name": "Deybi Jesus Vicioso Rodriguez",
        "matricula": "2022-0030",
        "bio": "El código convierte ideas en realidad.",
    },
    {
        "name": "Ima Rodriguez Rancier",
        "matricula": "2021-1621",
        "bio": "Cada error es una lección.",
    },
    {
        "name": "Juan Daniel Alcantara Oviedo",
        "matricula": "2022-1320",
        "bio": "Programar es pensar en soluciones.",
    },  
    {
        "name": "Edward Alexander Sánchez García",
        "matricula": "2021-0081",
        "bio": "Crear software es crear futuro.",
    },
    {
        "name": "Marcos José Morillo Suarez",
        "matricula": "2022-0113",
        "bio": "Un buen código es claro y eficiente.",
    },
    {
        "name": "Misael Roman Naranjo Tejada",
        "matricula": "2022-0113",
        "bio": "Cada línea de código cuenta.",
    },
        {
        "name": "Deivi Nicolás Mora Rodríguez",
        "matricula": "2021-1625",
        "bio": "La innovación nace del código.",
    },
    {
        "name": "Luis Ernesto Casilla Terrero",
        "matricula": "2023-0604",
        "bio": "El código no tiene fronteras.",
    },
    {
        "name": "Anthony Feliz",
        "matricula": "2021-0615",
        "bio": "La tecnología transforma el mundo.",
    },
]

# Crear ventana
root = tk.Tk()
root.title("Acerca de Nosotros")
root.configure(bg="#7A98B2")

title_label = tk.Label(root, text="Acerca de Nosotros", font=("Arial", 20, "bold"), fg="white", bg="#7A98B2")
title_label.pack(pady=10)


frame = tk.Frame(root, bg="#7A98B2")
frame.pack()

# Ajustes de tamaño de las tarjetas
CARD_WIDTH = 310  
CARD_HEIGHT = 180  


image_refs = []

# Cargar datos en la interfaz en filas de 2
for i in range(0, len(developers), 2):
    row_frame = tk.Frame(frame, bg="#7A98B2")  
    row_frame.pack(pady=10)  

    for j in range(2):
        if i + j < len(developers):
            dev = developers[i + j]

            card = tk.Frame(row_frame, bg="white", padx=10, pady=10, bd=2, relief="raised", width=CARD_WIDTH, height=CARD_HEIGHT)
            card.pack(side="left", padx=15) 
            card.pack_propagate(False) 

            name_label = tk.Label(card, text=dev["name"], font=("Arial", 14, "bold"), fg="#005BAC", bg="white", wraplength=250)
            name_label.pack()

            matricula_label = tk.Label(card, text=f"Matrícula: {dev['matricula']}", font=("Arial", 12), fg="#005BAC", bg="white")
            matricula_label.pack()

            bio_label = tk.Label(card, text=dev["bio"], font=("Arial", 10), wraplength=250, fg="#333333", bg="white")
            bio_label.pack()

# Ejecutar aplicación
root.mainloop()
