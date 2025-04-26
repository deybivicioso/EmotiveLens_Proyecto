from scanner import escaneo
from result_scanner import mostrar_resultados_con_grafico

if __name__ == "__main__":
    emociones = escaneo()
    mostrar_resultados_con_grafico(emociones)