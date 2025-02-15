import subprocess
import sys
from pathlib import Path

# Obtener la carpeta principal del proyecto (Raíz)
project_root = Path(__file__).resolve().parent

# Ruta de entrada.py dentro de la carpeta 'main'
entrada_path = project_root / "main" / "entrada.py"

# Ejecutar entrada.py
subprocess.run([sys.executable, str(entrada_path)])
