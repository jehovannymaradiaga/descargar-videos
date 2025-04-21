import os

from yt_dlp import YoutubeDL

####################################################################################

def cargar_lista_urls():
    print("\n=== Cargar Lista de URLs ===")
    
    # Solicitar al usuario la ruta del archivo
    ruta_archivo = input("Ingrese la ruta del archivo .txt con las URLs: ")
    
    # Validar si el archivo existe
    if not os.path.isfile(ruta_archivo):
        print("Error: El archivo no existe. Por favor, intente nuevamente.")
        return
    
    # Validar si el archivo tiene extensión .txt
    if not ruta_archivo.endswith(".txt"):
        print("Error: El archivo debe tener extensión .txt.")
        return
    
    try:
        # Leer las URLs del archivo
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            urls = [linea.strip() for linea in archivo if linea.strip()]
        
        # Verificar si se encontraron URLs
        if not urls:
            print("Error: El archivo está vacío o no contiene URLs válidas.")
            return
        
        print(f"\nSe cargaron {len(urls)} URLs del archivo:")
        for i, url in enumerate(urls, 1):
            print(f"{i}. {url}")
        
        # Confirmar si el usuario desea iniciar las descargas
        confirmar = input("\n¿Desea comenzar a descargar estos videos? (s/n): ").lower()
        if confirmar != "s":
            print("Operación cancelada.")
            return
        
        # Configurar las opciones de descarga con yt-dlp
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'progress_hooks': [progreso_descarga],
            'outtmpl': '%(title)s.%(ext)s'  # Guardar con el título del video
        }
        
        # Descargar cada URL
        with YoutubeDL(ydl_opts) as ydl:
            for url in urls:
                try:
                    print(f"\nDescargando: {url}")
                    ydl.download([url])
                except Exception as e:
                    print(f"Error al descargar {url}: {e}")
        
        print("\nTodas las descargas se han completado.")
    
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

def progreso_descarga(d):
    if d['status'] == 'downloading':
        print(f"\rProgreso: {d['_percent_str']} - Velocidad: {d['_speed_str']} - Tiempo restante: {d['_eta_str']}", end='')
    elif d['status'] == 'finished':
        print("\nDescarga completada.")


#######################################################################################


def descargar_por_url():
    print("\n=== Descargar por URL ===")
    
    # Solicitar al usuario la URL del video
    url = input("Ingrese la URL del video: ").strip()
    
    # Validar la URL
    if not url:
        print("Error: No se ingresó una URL. Por favor, intente nuevamente.")
        return
    
    try:
        # Configurar las opciones de descarga con yt-dlp
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'progress_hooks': [progreso_descarga],
            'outtmpl': '%(title)s.%(ext)s'  # Guardar con el título del video
        }
        
        # Descargar el video
        print(f"\nIniciando la descarga de: {url}")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print("\nDescarga completada con éxito.")
    
    except Exception as e:
        print(f"Error al descargar el video: {e}")    
    
########################################################################################

def buscar_y_descargar_por_nombre():
    print("\n=== Buscar y Descargar por Nombre ===")
    
    # Solicitar al usuario el nombre o palabra clave del video
    nombre_video = input("Ingrese el nombre o palabra clave para buscar: ").strip()
    
    # Validar que el nombre no esté vacío
    if not nombre_video:
        print("Error: No se ingresó ningún nombre. Por favor, intente nuevamente.")
        return
    
    try:
        # Configurar las opciones de búsqueda con yt-dlp
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'quiet': True,  # Suprimir la salida innecesaria
            'extract_flat': True,  # Solo obtener los resultados de la búsqueda (sin descargar aún)
        }
        
        # Realizar la búsqueda
        with YoutubeDL(ydl_opts) as ydl:
            resultados = ydl.extract_info(f"ytsearch:{nombre_video}", download=False)['entries']
        
        # Verificar si se encontraron resultados
        if not resultados:
            print("No se encontraron videos que coincidan con la búsqueda.")
            return
        
        # Mostrar los resultados
        print(f"\nSe encontraron {len(resultados)} resultados para '{nombre_video}':")
        for i, video in enumerate(resultados, 1):
            print(f"{i}. {video['title']} - {video['url']}")
        
        # Solicitar al usuario seleccionar un video
        seleccion = input("\nSeleccione el número del video a descargar: ").strip()
        
        # Validar la selección
        if not seleccion.isdigit() or not 1 <= int(seleccion) <= len(resultados):
            print("Selección no válida. Operación cancelada.")
            return
        
        # Obtener la URL del video seleccionado
        video_seleccionado = resultados[int(seleccion) - 1]
        url_video = video_seleccionado['url']
        
        # Descargar el video seleccionado
        print(f"\nIniciando la descarga de: {video_seleccionado['title']}")
        ydl_opts['progress_hooks'] = [progreso_descarga]
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url_video])
        
        print("\nDescarga completada con éxito.")
    
    except Exception as e:
        print(f"Error al realizar la búsqueda o descargar el video: {e}")
    
########################################################################################

def salir():
    print("Gracias por usar el descargador de videos. ¡Hasta luego!")
    exit()

def mostrar_menu():
    print("\n=== Menú Principal ===")
    print("1. Cargar lista de URLs")
    print("2. Descargar por URL")
    print("3. Buscar y descargar por nombre")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cargar_lista_urls()
        elif opcion == "2":
            descargar_por_url()
        elif opcion == "3":
            buscar_y_descargar_por_nombre()
        elif opcion == "4":
            salir()
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()
