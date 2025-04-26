import webview
import time
import keyboard  # Necesitarás instalar este paquete
from pathlib import Path
from screeninfo import get_monitors

# Obtener la carpeta principal del proyecto
project_root = Path(__file__).resolve().parent.parent

url_encuesta = "https://www.surveymonkey.com/r/HD56TBB"
url_resultados = "https://es.surveymonkey.com/results/SM-51F53HyLR20KS0Km7bpZwQ_3D_3D/"

def control_boton(window):
    time.sleep(3)  # Esperar a que la página cargue

    inject_button_js = """
    if (!document.getElementById("verResultadosBtn")) {
        let btn = document.createElement("button");
        btn.id = "verResultadosBtn";
        btn.innerText = "VER RESULTADOS";
        btn.style.position = "fixed";
        btn.style.bottom = "20px";
        btn.style.right = "20px";
        btn.style.padding = "10px 15px";
        btn.style.fontSize = "16px";
        btn.style.backgroundColor = "#16CD7B";
        btn.style.color = "white";
        btn.style.border = "none";
        btn.style.borderRadius = "5px";
        btn.style.zIndex = "9999";
        btn.onclick = function(){
            window.location.href = "%s";
        };
        document.body.appendChild(btn);
    }
    """ % url_resultados

    window.evaluate_js(inject_button_js)

    # Esperar a que el usuario presione "q" para cerrar la ventana
    while True:
        if keyboard.is_pressed('q'):  # Detecta la tecla 'q'
            window.destroy()  # Cierra la ventana
            break

if __name__ == '__main__':
    window = webview.create_window("Encuesta", url_encuesta)
    webview.start(func=control_boton, args=(window,))
