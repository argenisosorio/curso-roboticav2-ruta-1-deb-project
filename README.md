# Curso de Robótica - Ruta 1, empaquetado con Python PyWebView en DEB

-----

1. Construir el paquete .deb:

$ dpkg-deb --build app curso-roboticav2-ruta-1-deb-project_1.0_all.deb

2. Instala el paquete gestionando las dependencias necesarias:

$ sudo apt update

$ sudo apt install ./curso-roboticav2-ruta-1-deb-project_1.0_all.deb
