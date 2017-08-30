# coding= utf-8
# !/usr/bin/env python
# -*- codcivdoning: utf-8 -*-
from random import randint
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
edad = open('edades.txt').read().splitlines()
finished = 0
finishing = 0
turno = 0
civtemp = 0                         # Variable temporal para todos los repartos
reparto = 0                         # Variable que determina si la generación inicial ha terminado y se puede salir del while (lin= )
civdon = [0, 0, 0, 0, 0]
civdonnum = 0                          # Variable que muestra en que lugar de las 5 civilizaciones se encuentra la generación
civ = [0, 0, 0, 0, 0]
zonaclaimed = [0, 0, 0, 0, 0, 0, 0, 0]
civzona = [0, 0, 0, 0, 0]
poblacion = [0, 0, 0, 0, 0]
dinero = [0, 0, 0, 0, 0]
belicismo = [0, 0, 0, 0, 0]
sabiduria = [0, 0, 0, 0, 0]
agricultura = [0, 0, 0, 0, 0]
industria = [0, 0, 0, 0, 0]
niveltecnologico = [0, 0, 0, 0, 0]
podermilitar = [0, 0, 0, 0, 0]
nedad = 0
evento = 0
zona = ["Mediterráneo", "Oriente Próximo", "Europa Oeste", "Europa Este", "Norte de Asia", "Australia", "Asia Este",
        "Sudamérica", "Norteamérica"]
zonanot = []
civnot = ["Arabia", "Grecia", "Roma", "Egipto", "Mesopotamia"]
civnotnot = []


def comienzopartida():
    global civ
    global civzona
    global turno
    global agricultura

    print("Las primeras tribus de las civilizaciones se reúnen entre ellas")
    print(civ[0], " se instala en ", civzona[0])
    print(civ[1], ", por su parte, deja el modelo nómada en", civzona[1])
    print(civ[2], " toma", civzona[2], " como su hogar.")
    print("Las tierras de ", civzona[3], "pertenecen a", civ[3])
    print("Por último, las fuerzas de ", civ[4], " se asientan en", civzona[4])
    while turno != 5:
        poblacion[turno] = 10
        agricultura[turno] = 10
        niveltecnologico[turno] = 0.5
        turno = turno + 1


def comienzoturno():
    global nedad
    global finishing
    global turno
    if not nedad > 62:
        nedad = nedad + 1
        print("Estamos en", edad[nedad])
        turno = 0
    else:
        finishing = 1


def progresopoblacion():
    global poblacion
    global turno
    global agricultura
    global dinero
    if poblacion[turno] > (agricultura[turno] * 100):
        perdida = poblacion[turno] * (randint(25, 75) / 100)
        poblacion[turno] = poblacion[turno] - perdida
    else:
        poblacion[turno] = poblacion[turno] * (agricultura[turno] * 0.75)
    print("La población de", civ[turno], " es de %.0f" % poblacion[turno])


def finish():
    global finished
    finished = 1
    exit()


def progresoturno():
    global turno
    while turno != 5:
        if civ[turno] != 0:
            progresotecnologico()
            progresomilitar()
            progresoeconomico()
            progresopoblacion()
            evento = randint(1, 100)
            if evento == 1:
                eventohambruna()
            if poblacion[turno] <= 0:
                print("----La civilización de ", civ[turno],
                      "ha desaparecido. Sus logros serán utilizados quizás por el futuro----")
                civ[turno] = 0
        turno = turno + 1


def progresotecnologico():
    global sabiduria
    global niveltecnologico
    global agricultura
    global industria
    avance = (dinero[turno] * 0.01 * (sabiduria[turno] * 0.05)) / 100 * (poblacion[turno] * 0.02)
    niveltecnologico[turno] = avance + niveltecnologico[turno]
    print("El nivel tecnológico de", civ[turno], " es de %.2f" % niveltecnologico[turno])


def progresoeconomico():
    global agricultura
    global industria
    global turno
    global civ
    global dinero
    global niveltecnologico
    avance = (agricultura[turno] * 0.03 + industria[turno] * 0.6) * (niveltecnologico[turno] * 0.0002) * (
    poblacion[turno] * 0.002)
    dinero[turno] = dinero[turno] + avance
    print(civ[turno], " ha conseguido %.2f" % avance)
    print(civ[turno], " tiene %.2f" % dinero[turno])


def eventohambruna():
    global edad
    global nedad
    global civ
    global turno
    global poblacion
    global agricultura
    print("Hambruna en los límites de", civ[turno], " en el año", edad[nedad],
          ". Su economía y población han decrecido. El mundo está expectante.")
    perdida = (randint(25, 75) / 100)
    agricultura[turno] = agricultura[turno] * perdida


def progresomilitar():
    global dinero
    global podermilitar
    global belicismo
    podermilitar[turno] = podermilitar[turno] + (niveltecnologico[turno] * 0.05) * (
    dinero[turno] * (belicismo[turno] * 0.005))
    dinero[turno] = dinero[turno] - (belicismo[turno] * (dinero[turno] * 0.01))
    print("El poder militar de", civ[turno], " es de %.2f" % podermilitar[turno])


from funciones import repartofuncion
from funciones import repartozonas
from funciones import caracteriscticas

print("Generando civilizaciones en sus lugares.")
civ[0] = repartofuncion()
civ[1] = repartofuncion()
civ[2] = repartofuncion()
civ[3] = repartofuncion()
civ[4] = repartofuncion()
civzona[0] = repartozonas()
civzona[1] = repartozonas()
civzona[2] = repartozonas()
civzona[3] = repartozonas()
civzona[4] = repartozonas()
print("Concediendo características a cada civilización")
belicismo[0] = caracteriscticas()
belicismo[1] = caracteriscticas()
belicismo[2] = caracteriscticas()
belicismo[3] = caracteriscticas()
belicismo[4] = caracteriscticas()
sabiduria[0] = caracteriscticas()
sabiduria[1] = caracteriscticas()
sabiduria[2] = caracteriscticas()
sabiduria[3] = caracteriscticas()
sabiduria[4] = caracteriscticas()
comienzopartida()
while not finished:
    if finishing == 1:
        finish()
    else:
        comienzoturno()
        progresoturno()
