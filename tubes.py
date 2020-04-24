#import library
import random as random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#------------Data comment-----------------
    #isi={'posX':[],'posY':[],'stat_sehat':[],'stat_imun':[],'waktu_infeksi':[]}
    #dataAwal=pd.DataFrame({'posX','posY','stat_sehat','stat_imun','waktu_infeksi'})
    #print(dataAwal)
#------------Function Program---------------
def dataPreparation(n,rasio):
    posX=[];posY=[];stat_sehat=[];stat_imun=[];waktu_infeksi=[]
    dataAwal=pd.DataFrame()
    prob_terinfeksi=n*rasio
    for i in range (n):
        posX.append(0)
        posY.append(0)
        waktu_infeksi.append(0)
        stat_imun.append('imun lemah')
        #terdapat hasil dari prob_terinfeksi yang terinfeksi (200*0.05)
        if(i<prob_terinfeksi):
            stat_sehat.append('terinfeksi')
        else:
            stat_sehat.append('belum terinfeksi')
        
    dataAwal.insert(0,'posX',posX)
    dataAwal.insert(1,'posY',posY)
    dataAwal.insert(2,'status sehat',stat_sehat)
    dataAwal.insert(3,'status imun',stat_imun)
    dataAwal.insert(4,'waktu terinfeksi',waktu_infeksi)
    print(dataAwal)    
    return dataAwal

#--------------Variabel Program-------------
xMin = -20
xMax = 20
yMin = -20 
yMax = 20
x_range = xMax - xMin
y_range = yMax - yMin

nIndividu = 200
rasioIndividuTerinfeksi = 5/100
probIndividuBergerak = 8/100
waktuPulih = 10
nHari=100
ruangSimulasi_xMax=20
ruangSimulasi_xMin=-20
ruangSimulasi_yMax=20
ruangSimulasi_yMin=-20
rs_xRange= ruangSimulasi_xMax - ruangSimulasi_xMin
rx_yRange= ruangSimulasi_yMax - ruangSimulasi_yMin


#--------------Main Program-------------
initialData=dataPreparation(nIndividu,rasioIndividuTerinfeksi)


