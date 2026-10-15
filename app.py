import os
import sys
import webview

def get_html_path():
    # Obtiene la ruta absoluta de la carpeta 'html'
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, 'html', 'index.html')

if __name__ == '__main__':
    html_file = get_html_path()

    # Crea la ventana apuntando al index.html
    window = webview.create_window(
        title='Curso de Robótica - Ruta 1',
        url=f'file://{html_file}',
        width=1024,
        height=768,
        resizable=True
    )

    # Inicia la app usando GTK/WebKit nativo en Linux
    webview.start(gui='gtk')
