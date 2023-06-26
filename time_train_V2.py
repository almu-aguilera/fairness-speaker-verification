import sys, os, argparse, socket, csv
from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io 

parser = argparse.ArgumentParser()
parser.add_argument("-path_data", "--dataset_path", help="Path donde se encuentra los datos wav")
#dataset_path = '/var/data/db/FairVoice/FairVoice/FairVoice/Spanish'
parser.add_argument("-f", "--file", help="Nombre de archivo txt, lista a procesar")
#Spanish_train.txt
args = parser.parse_args()

def time_train_process():
    print("Empezando el programa")

    dataset_path = args.dataset_path 
    time=[]
    f = open (args.file,'r')
    lineas = f.readlines()
    lenght =len(lineas)

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
    return time_data

def main():
    time_data = time_train_process() 

    horas=int(time_data/3600)
    time_data-=horas*3600
    minutos=int(time_data/60)
    time_data-=minutos*60
 
    print("Tiempo de entrenamiento: %s:%s:%s" % (horas,minutos,time_data))
    #print(f"Tiempo de entrenamiento = {time_data}s")

main()

