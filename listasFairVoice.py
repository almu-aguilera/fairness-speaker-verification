import datetime
import os
import pandas as pd
import random
import argparse
import sys, argparse, csv

def train_test(fileTrain, fileTest, idioma, path, num):
    nameTest='/test_'+('{}_'.format(num))+('{}.txt'.format(idioma))
    nameTrain='/train_'+('{}_'.format(num))+('{}.txt'.format(idioma))
    fTrain= open('./'+path + nameTrain, 'w')
    fTest = open('./'+path+ nameTest, 'w')
    N=0; M=0
    with open(fileTrain, newline='') as FileTrain: 
        readerTrain = csv.reader(FileTrain, delimiter=",")
        for lineTrain in readerTrain:
            if N>0:
                Ldiv=lineTrain[0].split('/')
                fTrain.write(Ldiv[0]+ ' ' + lineTrain[0] + '\n')
            N=N+1

    with open(fileTest, newline='') as FileTest:
        readerTest = csv.reader(FileTest, delimiter=',')
        for lineTest in readerTest:
            if M>0: 
                fTest.write(lineTest[6]+ ' ' + lineTest[0] + ' ' + lineTest[1] + '\n')
            M=M+1

    fTest.close()
    fTrain.close()


def division_genero_test(file, idioma, path, num):
    testF='/female_'+('{}_'.format(num))+('{}.txt'.format(idioma))
    testM='/male_'+('{}_'.format(num))+('{}.txt'.format(idioma))
    ff2 = open('./'+path + testF, 'w')
    fm2 = open('./'+path + testM, 'w')
    M=0

    with open(file, newline='') as File2:
        reader2 = csv.reader(File2, delimiter=',')
        for line1 in reader2:
            if M>=0:
                if (line1[4]=='' or line1[4]=='female'):
                    if (line1[5]=='' or line1[5]=='female'):
                        ff2.write(line1[6] + ' ' + line1[0] + ' ' + line1[1] + '\n')
                elif (line1[4]=='' or line1[4]=='male'):
                    if (line1[5]=='' or line1[5]=='male'):
                        fm2.write(line1[6] + ' ' + line1[0] + ' ' + line1[1] + '\n')
            M=M+1

    ff2.close()
    fm2.close()

def division_edad(file, idioma, path, num):
    testO='/old_'+('{}_'.format(num))+('{}.txt'.format(idioma))
    testY='/young_'+('{}_'.format(num))+('{}.txt'.format(idioma))
    fo1 = open('./'+path + testO, 'w')
    fy1 = open('./'+path + testY, 'w')
    N=0

    with open(file, newline='') as File1:
        reader1 = csv.reader(File1, delimiter=',')
        for line1 in reader1:
            if N>=0:
                if line1[2]=='' or line1[2] =='old': 
                    if line1[3]=='' or line1[3] =='old': 
                            fo1.write(line1[6] + ' ' + line1[0] + ' ' + line1[1] + '\n')
                elif (line1[2]=='' or line1[2]=='young'):
                    if (line1[3]=='' or line1[3]=='young'):
                        fy1.write(line1[6] + ' ' + line1[0] + ' ' + line1[1] + '\n')
            N=N+1

    fo1.close()
    fy1.close()

def division_edad(file, idioma, path, num):
    testOm='/old_male_'+('{}_'.format(num))+('{}.txt'.format(idioma))
    testYm='/young_male_'+('{}_'.format(num))+('{}.txt'.format(idioma))
    testOf='/old_female_'+('{}_'.format(num))+('{}.txt'.format(idioma))
    testYf='/young_female_'+('{}_'.format(num))+('{}.txt'.format(idioma))
    fo1 = open('./'+path + testOm, 'w')
    fy1 = open('./'+path + testYm, 'w')
    fo2 = open('./'+path + testOf, 'w')
    fy2 = open('./'+path + testYf, 'w')
    N=0

    with open(file, newline='') as File1:
        reader1 = csv.reader(File1, delimiter=',')
        for line1 in reader1:
            if N>=0:
                if line1[2] =='old' or line1[3] =='old': 
                    if line1[4]=='female'or line1[5]=='female':
                        fo2.write(line1[6] + ' ' + line1[0] + ' ' + line1[1] + '\n')
                    elif line1[4]=='male'or line1[5]=='male':
                        fo1.write(line1[6] + ' ' + line1[0] + ' ' + line1[1] + '\n')
                elif line1[2] =='young' or line1[3] =='young': 
                    if line1[4]=='female'or line1[5]=='female':
                        fy2.write(line1[6] + ' ' + line1[0] + ' ' + line1[1] + '\n')
                    elif line1[4]=='male'or line1[5]=='male':
                        fy1.write(line1[6] + ' ' + line1[0] + ' ' + line1[1] + '\n')
                N=N+1

    fo1.close()
    fy1.close()
    fo2.close()
    fy2.close()

def main():
    parser = argparse.ArgumentParser(description='Generate file Train and test')
    parser.add_argument('--lenguaje', dest='lenguaje', default='English', type=str, action='store', help='')
    parser.add_argument('--num_of_spk', dest='num_of_spk', default=1020, type=int, action='store', help='')
    parser.add_argument("--fileTest", "--fileTr", help="archivo csv") 
    parser.add_argument("--fileTrain", "--fileTe", help="archivo csv") 
    parser.add_argument("--path_data", "--dataset_path", help="Path donde guardas")
    args = parser.parse_args()

    train_test(args.fileTrain, args.fileTest, args.lenguaje, args.path_data, args.num_of_spk)
    division_genero_test(args.fileTest, args.lenguaje, args.path_data, args.num_of_spk)
    division_edad(args.fileTest, args.lenguaje, args.path_data, args.num_of_spk)
    division_edad_genero(args.fileTest, args.lenguaje, args.path_data, args.num_of_spk)

if __name__== "__main__":
  main()
