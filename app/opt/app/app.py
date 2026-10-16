# Script para iniciar un servidor local y abrir la aplicación eXeLearning en el
# navegador predeterminado.

import os
import sys
import threading
import time
import webbrowser
import bottle

# Define la aplicación Bottle para servir los archivos estáticos de eXeLearning
app_bottle = bottle.Bottle()

def get_base_dir():
    """
    Obtiene el directorio base del script, considerando si está ejecutándose
    como un ejecutable congelado (por ejemplo, con PyInstaller) o como un script
    normal.
    """
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

@app_bottle.route('/<filepath:path>')
def server_static(filepath):
    """
    Sirve archivos estáticos desde el directorio 'html' de eXeLearning.
    """
    html_dir = os.path.join(get_base_dir(), 'html')
    return bottle.static_file(filepath, root=html_dir)

@app_bottle.route('/')
def index():
    """
    Sirve el archivo index.html como página principal.
    """
    html_dir = os.path.join(get_base_dir(), 'html')
    return bottle.static_file('index.html', root=html_dir)

def run_server():
    # Ejecuta el servidor local en el puerto 8080 (sin quiet=True para ver registros en consola)
    bottle.run(app_bottle, host='127.0.0.1', port=8080)

if __name__ == '__main__':
    # Inicia el servidor local en un hilo secundario
    t = threading.Thread(target=run_server, daemon=True)
    t.start()

    url = 'http://127.0.0.1:8080/'

    # Da un breve respiro al hilo para asegurar que el servidor esté listo
    time.sleep(0.5)

    # Abre la aplicación en el navegador predeterminado
    webbrowser.open(url)

    # Mantiene el script principal activo mientras el servidor corre
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)
