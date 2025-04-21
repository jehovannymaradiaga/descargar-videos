# 📥 YouTube Video Downloader con `yt-dlp` (Interfaz en Consola)

Este script en Python permite descargar videos de YouTube mediante diferentes métodos utilizando la biblioteca [`yt-dlp`](https://github.com/yt-dlp/yt-dlp), una herramienta avanzada para descargas de video/audio. Ofrece una interfaz de línea de comandos simple e intuitiva con tres funciones principales:

---

## 🚀 Funcionalidades

1. **📄 Cargar lista de URLs desde un archivo `.txt`:**  
   Permite cargar múltiples enlaces desde un archivo de texto y descargarlos uno por uno.

2. **🔗 Descargar un solo video desde una URL:**  
   Descarga un video ingresando directamente su enlace.

3. **🔍 Buscar por nombre en YouTube y seleccionar qué video descargar:**  
   Realiza una búsqueda por palabras clave, muestra los resultados, y permite elegir un video para descargar.

---

## 📦 Requisitos

- Python 3.7 o superior
- Paquete `yt-dlp`

### Instalación de dependencias

```bash
pip install yt-dlp

# Uso del script
python menu.py

=== Menú Principal ===
1. Cargar lista de URLs
2. Descargar por URL
3. Buscar y descargar por nombre
4. Salir


▶️ Opción 1: Cargar lista de URLs
Debes tener un archivo .txt con una URL por línea.

El programa leerá el archivo, mostrará cuántas URLs se detectaron y pedirá confirmación antes de comenzar la descarga.

▶️ Opción 2: Descargar por URL
Ingresa la URL de un video específico y se iniciará la descarga del video con la mejor calidad disponible.

▶️ Opción 3: Buscar y descargar por nombre
Ingresa una palabra clave o título de video.

El programa buscará en YouTube y listará resultados.
Elige el número del video que deseas descargar.

⚙️ Configuración Interna
Descargas en la mejor calidad disponible (bestvideo+bestaudio).

Archivos guardados con el título del video como nombre de archivo.

Muestra el progreso de descarga, velocidad y tiempo estimado restante.

✍️ Autor
Jehovanny Maradiaga
GitHub: @jehovannymaradiaga

