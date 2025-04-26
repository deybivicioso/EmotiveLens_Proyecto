import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
import mysql.connector


modo_seleccionado = {
    "Detallado":    {"color": "#FFFACD", "emoji": "📃"},
    "Simple":       {"color": "#ADD8E6", "emoji": "🎭"},
}

def obtener_resultados():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Deiinik6",  # Cambia según tu configuración
            database="scanner"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT modo, timestamp FROM seleccion ORDER BY timestamp DESC")
        selecciones = cursor.fetchall()
        conexion.close()
        return selecciones
    except mysql.connector.Error as error:
        print("Error de conexión:", error)
        return []

def crear_historial_seleccion_ui():
    ventana = tk.Tk()
    ventana.title("Historial")
    ventana.state("zoomed")
    ventana.configure(bg="white")

    # Barra superior
    barra = tk.Frame(ventana, bg="#7A9EB1", height=50)
    barra.pack(fill="x")

    btn_volver = tk.Button(barra, text="←", font=("Arial", 24, "bold"), bg= "#7A9EB1", fg="white", relief="flat", command=ventana.destroy)
    btn_volver.pack(side="left", padx=10, pady=10)

    tk.Label(barra, text="HISTORIAL DE SELECCION", font=("Arial", 14, "bold"), bg="#7A9EB1", fg="white", padx=20).pack(side="left", pady=10)

    # Contenedor con scroll
    contenedor_canvas = tk.Canvas(ventana, bg="white", highlightthickness=0)
    scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=contenedor_canvas.yview)
    contenedor_scroll = tk.Frame(contenedor_canvas, bg="white")

    contenedor_scroll.bind(
        "<Configure>",
        lambda e: contenedor_canvas.configure(scrollregion=contenedor_canvas.bbox("all"))
    )

    contenedor_canvas.create_window((0, 0), window=contenedor_scroll, anchor="nw")
    contenedor_canvas.configure(yscrollcommand=scrollbar.set)

    contenedor_canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Cargar datos de la BD
    datos = obtener_resultados()

    for modo, fecha_hora in datos:
        estilo = modo_seleccionado.get(modo)
        
        if estilo:
            color_fondo = estilo["color"]
            emoji = estilo["emoji"]
        else:
           
            color_fondo = "#FFFFFF"
            emoji = "❓"
        

        frame = tk.Frame(contenedor_scroll, bg=color_fondo, bd=2, relief="solid")
        frame.pack(padx=20, pady=10, fill="x")

        # Subcontenedor
        interno = tk.Frame(frame, bg=color_fondo)
        interno.pack(fill="x", padx=400, pady=10)

        # Emoji o ícono a la izquierda
        tk.Label(interno, text= emoji, font=("Arial", 50), bg=color_fondo).pack(side="left", padx=10)

        # Info a la derecha
        info = tk.Frame(interno, bg=color_fondo)
        info.pack(side="left", fill="both", expand=False)

        tk.Label(info, text=f"Modo Seleccionado: {modo}", font=("Arial", 16, "bold"), bg=color_fondo).pack(anchor="w")
        tk.Label(info, text=f"Fecha: {fecha_hora}", font=("Arial", 10, "italic"), bg=color_fondo, fg="gray").pack(anchor="w")

    ventana.mainloop()

crear_historial_seleccion_ui()