import scipy.io 
import sys, os, argparse, socket, csv
from os.path import dirname, join as pjoin
from scipy.io import wavfile

#MEJORAR ARCHIVO CON Parse arguments
parser = argparse.ArgumentParser()


print("Empezando el programa")
dataset_path = '/var/data/db/FairVoice/FairVoice/FairVoice/Spanish'
time=[]

archivo='./Esp_List/Spanish_train.txt'
#archivo='./Eng_List/E
f = open (archivo,'r')
lineas = f.readlines()
lenght =len(lineas)

#hacer algun tipo de bucle que recorra toda la lista train y obteniendo cada nombre, 
#en ese bucle hacer una lista de todo el tiempo y luego un sum 
print("Empezamos el bucle, puede tardar un poco")
for i in range(lenght):
    nombre=lineas[i]
    nombre=nombre.split(' ')
    wav_fname = pjoin(dataset_path, nombre[1])
    wav_fname = wav_fname.split('\n')
    samplerate, data = wavfile.read(wav_fname[0])
    longitud = data.shape[0]/samplerate
    time.append(longitud)

time_data=sum(time)
print(f"Tiempo de entrenamiento = {time_data}s")