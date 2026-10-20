# Curso de Robótica v2 - Ruta 1, empaquetado con Python PyWebView en DEB

**Generado e Instalado en:** Linux Debian 13.

-----

1. Construir el paquete .deb:

```bash
$ dpkg-deb --build app curso-roboticav2-ruta-1-deb-project_1.0_all.deb
```

2. Instala el paquete gestionando las dependencias necesarias:

```bash
$ sudo apt update
```

```bash
$ sudo apt install ./curso-roboticav2-ruta-1-deb-project_1.0_all.deb
```

-Nombre del paquete instalado: curso-roboticav2-ruta-1-deb

-Dependencias instaladas: python3-bottle, python3-webview

3. Eliminar la app instalada

```bash
$ sudo apt remove --purge curso-roboticav2-ruta-1-deb
```

4. Pasos opcionales de limpieza:

Si quieres eliminar las librerías o dependencias de Python que se instalaron
automáticamente junto con tu app y que ya ningún otro programa esté utilizando,
ejecuta:

```bash
$ sudo apt autoremove
```
