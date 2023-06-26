import sys, os, argparse, socket, csv
from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io 

parser = argparse.ArgumentParser()
#dataset_path = '/var/data/db/FairVoice/FairVoice/FairVoice/Spanish'
parser.add_argument("-f", "--file", help="Nombre de archivo txt, lista a procesar")
parser.add_argument("-path_data", "--dataset_path", help="Path donde se encuentra los datos wav")

args = parser.parse_args()
def time_train_process():
    i=1
    print("Empezando el programa")

    dataset_path = args.dataset_path 
    time=[]
    f = open (args.file,'r')
    lineas = f.readlines()
    lenght =len(lineas)

    print("Empezamos el bucle, puede tardar un poco")
    
    nombre=lineas[i]
    nombre=nombre.split(' ')
    wav_fname = pjoin(dataset_path, nombre[1])
    wav_fname = wav_fname.split('\n')
    samplerate, data = wavfile.read(wav_fname[0])
    longitud = data.shape[0]/samplerate
    time = longitud 

    Tiempo_total=lenght*time; 
    return Tiempo_total

def main():
    print('Iniciamos el programa')
    time = time_train_process()
    
    horas = int(time/3600)
    time = time - (horas*3600)
    minutos = int(time/60) 
    segundos = time - (minutos*60)
    print('Tiempo total de entranamiento: %s:%s:%s' %(horas, minutos, segundos))

main()

