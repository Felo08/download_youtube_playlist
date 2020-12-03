import pafy
import os
import sys
from tkinter import filedialog


def ingresar_url_playlist():
    urlplaylist = input("Ingrese la URL de la playlist: ")
    if not urlplaylist:
        print("No ingreso la URL de la playlist")
    else:
        playlist = pafy.get_playlist(urlplaylist)
        menu(playlist)

    sys.exit(0)


# ------------------------------- Fin ingresar_URL_playlist --------------------------------


def menu(playlist):
    ejecutar_programa = True
    while ejecutar_programa:
        opcion_escogida = input("""1) informacion sobre la playlist
        \n 2) descargar playlist (video y audio)
        \n 3) descargar playlist (solo video)
        \n 4) descargar playlist (solo audio)
        \n 5) salir
        \n opcion a escoger: """)

        if opcion_escogida == '1':
            informacion_playlist(playlist)
        elif opcion_escogida == "2":
            descargar_video_audio(playlist)
        elif opcion_escogida == "3":
            descargar_video(playlist)
        elif opcion_escogida == "4":
            descargar_audio(playlist)
        elif opcion_escogida == "5":
            ejecutar_programa = False
            break

# ------------------------------- Fin menu --------------------------------

def informacion_playlist(playlist):
    print("Titulo de la playlist: " + playlist['title'], end='\n')
    print("Numero de videos de la playlist: %s" % len(playlist['items']), end='\n')
    print("Autor de la playlist: " + playlist['author'] , end='\n \n')


# ------------------------------- Fin funcion informacion --------------------------------


# Funcion para descargar el video junto con el audio de los videos de la playlist

def descargar_video_audio(playlist):
    directorio = filedialog.askdirectory()
    if directorio != "":
        os.chdir(directorio)
    print(os.getcwd())

    desde_el_video = input("Desde el video: ")
    hasta_el_video = input("Hasta el video: ")

    if desde_el_video == '':
        desde_el_video = '0'

    if hasta_el_video == '':
        video_fin = len(playlist['items'])
    else:
        video_fin = int(hasta_el_video)

    video_inicio = int(desde_el_video)

    for i in range(video_inicio, video_fin):
        objeto_video = playlist['items'][i]['pafy']
        video_descargable = objeto_video.getbest()
        print("descargando el video numero: %s" % (i + 1))
        descarga = video_descargable.download()


# ------------------------------- Fin funcion video y audio --------------------------------


# Funcion para descargar solo el video, sin audio, de los videos de la playlist

def descargar_video(playlist):
    directorio = filedialog.askdirectory()
    if directorio != "":
        os.chdir(directorio)
    print(os.getcwd())

    desde_el_video = input("Desde el video: ")
    hasta_el_video = input("Hasta el video: ")

    if desde_el_video == '':
        desde_el_video = '0'

    if hasta_el_video == '':
        video_fin = len(playlist['items'])
    else:
        video_fin = int(hasta_el_video)

    video_inicio = int(desde_el_video)

    for i in range(video_inicio, video_fin):
        objeto_video = playlist['items'][i]['pafy']
        video_descargable = objeto_video.getbestvideo()
        print("descargando el video numero: %s" % (i + 1))
        descarga = video_descargable.download()


# ------------------------------- Fin funcion solo video --------------------------------


# Funcion para descargar solo el audio de los videos de la playlist

def descargar_audio(playlist):
    directorio = filedialog.askdirectory()
    if directorio != "":
        os.chdir(directorio)
    print(os.getcwd())

    desde_el_video = input("Desde el video: ")
    hasta_el_video = input("Hasta el video: ")

    if desde_el_video == '':
        desde_el_video = '0'

    if hasta_el_video == '':
        video_fin = len(playlist['items'])
    else:
        video_fin = int(hasta_el_video)

    video_inicio = int(desde_el_video)

    for i in range(video_inicio, video_fin):
        objeto_video = playlist['items'][i]['pafy']
        video_descargable = objeto_video.getbestaudio()
        print("descargando el video numero: %s" % (i + 1))
        descarga = video_descargable.download()


# ------------------------------- Fin funcion solo audio --------------------------------


def __main__():
    ingresar_url_playlist()


# ------------------------------- Fin main --------------------------------


__main__()
