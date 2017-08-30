# coding= utf-8
#!/usr/bin/env python
# -*- codcivdoning: utf-8 -*-
from random import randint
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
zona = ["Mediterráneo", "Oriente Próximo", "Europa Oeste", "Europa Este", "Norte de Asia", "Australia", "Asia Este", "Sudamérica", "Norteamérica"]
zonanot = []
civnotnot = [0, 0, 0, 0, 0]
civzona = [0, 0, 0, 0, 0]
civ = [0, 0, 0, 0, 0]
civnot = ["Arabia", "Grecia", "Roma", "Egipto", "Mesopotamia"]


def repartofuncion():
    global civdon
    global civnot
    global civnotnot
    civdonnum = 0
    while civdonnum != 1:
        civtemp = randint(0, 4)
        if civtemp == 0:
            if civnotnot[0] == 0:
                civtemp = civnot[0]
                civnotnot[0] = 1
                civdonnum = 1
        elif civtemp == 1:
            if civnotnot[1] == 0:
                civtemp = civnot[1]
                civnotnot[1] = 1
                civdonnum = 1
        elif civtemp == 2:
            if civnotnot[2] == 0:
                civtemp = civnot[2]
                civnotnot[2] = 1
                civdonnum = 1
        elif civtemp == 3:
            if civnotnot[3] == 0:
                civtemp = civnot[3]
                civnotnot[3] = 1
                civdonnum = 1
        elif civtemp == 4:
            if civnotnot[4] == 0:
                civtemp = civnot[4]
                civnotnot[4] = 1
                civdonnum = 1
    return civtemp


def repartozonas():
    global zona
    civtemp = randint(0, 8)
    if civtemp == 0:
        civtemp = zona[0]
        civdonnum = 1
    elif civtemp == 1:
        civtemp = zona[1]
        civdonnum = 1
    elif civtemp == 2:
        civtemp = zona[2]
        civdonnum = 1
    elif civtemp == 3:
        civtemp = zona[3]
        civdonnum = 1
    elif civtemp == 4:
        civtemp = zona[4]
        civdonnum = 1
    elif civtemp == 5:
        civtemp = zona[5]
        civdonnum = 1
    elif civtemp == 6:
        civtemp = zona[6]
        civdonnum = 1
    elif civtemp == 7:
        civtemp = zona[7]
        civdonnum = 1
    elif civtemp == 8:
        civtemp = zona[8]
        civdonnum = 1
    return civtemp


def caracteriscticas():
    civtemp = randint(0, 100)
    return civtemp