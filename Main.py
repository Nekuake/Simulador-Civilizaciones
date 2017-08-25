#!/usr/bin/env python
# -*- codcivdoning: utf-8 -*-
from random import randint                      #Para la aleatoriedad
finished = 0
civtemp= 0                                      #Variable temporal para todos los repartos
reparto = 0                                     #Variable que determina si la generación inicial ha terminado y se puede salir del while (lin= )
civdon = [0,0,0,0,0]
civdonnum = 0                                   #Variable que muestra en que lugar de las 5 civilizaciones se encuentra la generación
civ = [0,0,0,0,0]
zonaclaimed = [0,0,0,0,0,0,0,0]
civzona = [0,0,0,0,0]
pobciv = [0,0,0,0,0]
riqciv = [0,0,0,0,0]
nedad =  0
zona = ["Mediterráneo","Oriente Próximo","Europa Oeste","Europa Este","Norte de Asia","Australia","Asia Este","Sudamérica","Norteamérica"]
zonanot = []
civnot = ["Arabia","Grecia","Roma","Egipto","Mesopotamia"]
civnotnot = []
def comienzopartida ():
    global civ
    global civzona
    print("Las primeras tribus de las civilizaciones se reúnen entre ellas")
    print(civ[0], " se instala en ", civzona[0])
    print(civ[1], ", por su parte, deja el modelo nómada en", civzona[1])
    print(civ[2], " toma", civzona[2], " como su hogar.")
    print("Las tierras de ", civzona[3], "pertenecen a", civ[3])
    print("Por último, las fuerzas de ", civ[4], " se asientan en", civzona[4])
def comienzoturno ():
    global nedad
    nedad = nedad + 1
    print("Estamos en", edad[nedad])
from funciones import repartofuncion
from funciones import repartozonas
print("Generando civilizaciones en sus lugares.")
civ[0] = repartofuncion()
civ[1] = repartofuncion()
civ[2] = repartofuncion()
civ[3] = repartofuncion()
civ[4] = repartofuncion()
civzona[0] = repartozonas ()
civzona[1] = repartozonas ()
civzona[2] = repartozonas ()
civzona[3] = repartozonas ()
civzona[4] = repartozonas ()
comienzopartida()
