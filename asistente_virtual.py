import speech_recognition as sr
import subprocess as sub
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import keyboard
import os
import colors
from tkinter import *
from PIL import Image, ImageTk
from pygame import init, mixer





# nombre del asistente
name = "Talker"


# inicializando el sistema de voz
listener = sr.Recognizer()  # reconociendo de voz
engine = pyttsx3.init()  # inicializando el motor de voz

voices = engine.getProperty('voices')  # obteniendo las voces
# seleccionando la voz 0. sabina Desktop - Spanish (Mexico) 1. zira Desktop - English (united States)
engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 180)  # configuracion de la voz
engine.setProperty('volume', 0.7)  # volumen

sites = {
    "google": "https://www.google.com/",
    "youtube": "https://www.youtube.com/",
    "wikipedia": "https://es.wikipedia.org/",
    "facebook": "https://www.facebook.com/",
    "twitter": "https://twitter.com/",
    "instagram": "https://www.instagram.com/",
    "pinterest": "https://www.pinterest.com/",
    "amazon": "https://www.amazon.com/",
    "netflix": "https://www.netflix.com/",
    "spotify": "https://open.spotify.com/",
    "github": "https://github.com/login",
    "linkedin": "https://www.linkedin.com/",
    "gmail": "https://mail.google.com/",
    "outlook": "https://outlook.live.com/owa/",
    "yahoo": "https://mail.yahoo.com/",
    "google drive": "https://drive.google.com/",
    "google maps": "https://www.google.com/maps/",
    "google photos": "https://photos.google.com/",
    "traductor": "https://translate.google.com/",





}


def talk(text):  # funcion para hablar
    engine.say(text)  # hablando
    engine.runAndWait()  # ejecutando


def listen():  # funcion para escuchar
    try:
        with sr.Microphone() as source:  # conectando el microfono
            print("Escuchando...")
            audio = listener.listen(source)  # escuchando
            said = listener.recognize_google(
                audio, language="es")  # reconociendo
            said = said.lower()  # convertiendo a minusculas

            if name in said:
                said = said.replace(name, '')

    except:
        pass
    return said


def run_talker():
    talk("Hola, soy talker, tu asistente virtual")
    talk("¿Qué deseas hacer?")
    while True:
        said = listen()
        if 'reproduce' in said or 'reproducir' in said or 'coloca la cancion' in said or 'pon la cancion' in said:  # si dice reproducir o similares
            # eliminando la palabra reproducir
            music = said.replace('reproduce', '')
            # eliminando la palabra reproducir
            music = music.replace('reproducir', '')
            # eliminando la palabra reproducir
            music = music.replace('coloca la cancion', '')
            # eliminando la palabra reproducir
            music = music.replace('pon la cancion', '')
            # imprimiendo que esta reproduciendo
            print("Reproduciendo" + music)
            talk("Reproduciendo " + music)  # hablando
            pywhatkit.playonyt(music)  # reproduciendo la cancion
        elif 'pausar' in said or 'pausa' in said:  # si dice pausar o similares
            music = said.replace('pausar', '')  # eliminando la palabra pausar
            music = music.replace('pausa', '')  # eliminando la palabra pausar
            print("Pausando")  # imprimiendo que esta pausando
            talk("Pausando")  # hablando
            pywhatkit.pauseonyt()  # pausando la cancion
        elif 'silenciar' in said or 'silencio' in said or 'silencia la cancion' in said or 'mutear' in said:  # si dice silenciar o similares
            # eliminando la palabra silenciar
            music = said.replace('silenciar', '')
            # eliminando la palabra silencio
            music = music.replace('silencio', '')
            # eliminando la palabra silencio
            music = music.replace('mutea', '')
            # eliminando la palabra silencio
            music = music.replace('silencia la cancion', '')
            print("Silenciando")  # imprimiendo que esta silenciando
            talk("Silenciando")  # hablando
            pywhatkit.silentyt()  # silenciando
        elif 'suspender' in said or 'detener' in said or 'deten la cancion' in said:   # si dice detener o similares
            # eliminando la palabra detener
            music = said.replace('suspender', '')
            # eliminando la palabra detener
            music = music.replace('detener', '')
            # eliminando la palabra detener
            music = music.replace('deten la cancion', '')
            # eliminando la palabra detener
            music = music.replace('suspende', '')
            print("Deteniendo")  # imprimiendo que esta deteniendo
            talk("Deteniendo")  # hablando
            pywhatkit.stoponyt()  # deteniendo la cancion
        elif 'buscar' in said or 'que es' in said:
            search = said.replace('buscar', '')  # eliminando la palabra buscar
            search = search.replace('que es', '')  # eliminando la palabra busca
            wikipedia.set_lang("es")  # cambiando el idioma a español
            # buscando en wikipedia
            wiki = wikipedia.summary(search, sentences=2)
            print(search + ": " + wiki)  # imprimiendo la busqueda
            talk(wiki)  # hablando
        elif 'alarma' in said or 'colocar alarma' in said:
            alarm = said.replace('alarma', '')  # eliminando la palabra alarma
            # eliminando la palabra alarma
            alarm = alarm.replace('colocar alarma', '')
            alarm = alarm.strip()
            talk("Alarma programada a las " + alarm + "horas")  # hablando
            while True:  # bucle infinito
                if datetime.datetime.now().strftime("%H:%M") == alarm:  # si la hora actual es la hora programada
                    talk("Alarma sonando")  # hablando
                    talk("Despierta ")
                    mixer.init()  # inicializando el mixer
                    mixer.music.load("alarma.mp3")
                    mixer.music.play()  # reproduciendo la alarma
                    if keyboard.read_key() == "esc":
                        mixer.music.stop()
                        break
        # si dice detectar color o captura color o similares
        elif 'detectar color' in said or 'captura color' in said:
            talk("Capturando color")
            colors.capture()  # capturando el color
        elif 'abre' in said or 'abrir' in said:
            for site in sites:
                if site in said:
                    sub.call(f'start chrome.exe {sites[site]}', shell=True)
                    talk(f'Abriendo {site}')
        elif 'escribe' in said or 'escribir' in said:
            write = said.replace('escribe', '')
            write = write.replace('escribir', '')
            try:  # intentando
                with open('Nota.txt', 'a') as f:  # abriendo el archivo
                    write(f)  # escribiendo en el archivo
            except FileNotFoundError as e:  # si no se encuentra el archivo
                file = open('Nota.txt', 'w')  # creando el archivo
                write(file)  # escribiendo en el archivo

        elif 'terminar' in said or 'salir' in said:
            talk("Adios")
            break


def write(f):  # escribiendo en el archivo
    talk("¿Qué deseas escribir?")  # preguntando que desea escribir
    said_write = listen()  # escuchando lo que dice el usuario
    f.write(said_write + os.linesep)  # escribiendo en el archivo
    f.close()  # cerrando el archivo
    talk("listo, puedes revisarlo")  # hablando que esta listo
    sub.Popen("Nota.txt", shell=True)  # abriendo el archivo


if __name__ == '__main__':
    run_talker()


