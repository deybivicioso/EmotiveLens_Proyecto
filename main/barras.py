import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import mysql.connector
from datetime import datetime

def obtener_ultimos_resultados():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",         
            password="Deiinik6",  
            database="scanner"
        )
        cursor = conexion.cursor()

        # Obtener los últimos registros de resultados
        consulta = """
            SELECT emocion_predominante, SUM(cantidad) 
            FROM resultados
            GROUP BY emocion_predominante
            ORDER BY SUM(cantidad) DESC
        """
        cursor.execute(consulta)
        resultados = cursor.fetchall()

        conexion.close()

        return resultados

    except mysql.connector.Error as err:
        print(f"Error al conectar con la base de datos: {err}")
        return []

def mostrar_grafico_barras():
    resultados = obtener_ultimos_resultados()

    if not resultados:
        print("No se encontraron resultados.")
        return

    emociones = [fila[0].capitalize() for fila in resultados]
    cantidades = [fila[1] for fila in resultados]

    root = tk.Tk()
    root.title("Gráfico de Barras de Emociones")
    root.state("zoomed")

    top_bar = tk.Frame(root, bg="#7a98b2", height=50)
    top_bar.pack(fill="x")

    frame = tk.Frame(root, bg="white")
    frame.pack(expand=True, fill="both")

    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    ax.bar(emociones, cantidades, color='skyblue')
    ax.set_title('Resultados de Emociones', fontsize=20)
    ax.set_xlabel('Emociones', fontsize=14)
    ax.set_ylabel('Cantidad', fontsize=14)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Mostrar los valores encima de cada barra (convertir a float)
    for i, v in enumerate(cantidades):
        ax.text(i, float(v) + 0.5, str(v), ha='center', va='bottom', fontsize=12)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True)

    root.mainloop()

if __name__ == "__main__":
    mostrar_grafico_barras()

