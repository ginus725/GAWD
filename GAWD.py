import time
import requests
import os
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

print("\nBenvenuto nel GAWD (Ginus, Addons, Windows Defender), Addons realizzato per aggiungere l'IA a Windwos defender.")

time.sleep(3)
print("\nTu sei George giusto")

time.sleep(1)
print("ci ho azzeccato vero, essendo io un semi modello di AI posso vedere dentro il tuo dispositivo,")

time.sleep(2)
print("guardando il nome utente.")

time.sleep(3)
print("Per iniziare comuque, devi aprirmi con amministratore, che cosa ne pensi??")

admin = input()
time.sleep(2)
print("quindi tu dici che "+admin+" ??")

time.sleep(2)
print("\nDownload avviato, durera 3 minuti, non spegnere il computer")

def loading_animation():
    start_time = time.time()
    end_time = start_time + 180
    
    while time.time() < end_time:
        for i in range(4):
            print("Download in corso" + "." * i)
            time.sleep(0.5)
            print("\033[F\033[K", end="")
            time.sleep(0.5)

loading_animation()

print("programma installato a perfezione")
file_name = "GAWD.py"

if os.path.exists(file_name):
    os.remove(file_name)
    print("File eliminato con successo.")


