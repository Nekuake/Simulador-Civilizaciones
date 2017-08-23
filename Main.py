#!/usr/bin/env python
# -*- codcivdoning: utf-8 -*-
from random import randint                      #Para la aleatoriedad
reparto = 0                                     #Variable que determina si la generación inicial ha terminado y se puede salir del while (lin= )
civdon = [0,0,0,0,0]
civdonnum = 0                                   #Variable que muestra en que lugar de las 5 civilizaciones se encuentra la generación
civ = [0,0,0,0,0]
pobciv = [0,0,0,0,0]
zona = ["Mediterráneo","Oriente Próximo","Europa Oeste","Europa Este","Norte de Asia","Australia","Asia Este","Sudamérica","Norteamérica"]
civnot = ["Arabia","Grecia","Roma","Egipto","Mesopotamia"]
civnotnot = [0,0,0,0,0]
print("Generando civilizaciones en sus lugares.")
while reparto != 1:
    print("Eligiendo primera civilización")
    while civdonnum == 0:
        civ[0] = randint (0,4)
        if civ[0] == 0:
            if civnotnot[0] == 0:
                civ[0] = civnot[0]
                civnotnot[0] = 1
                civdonnum = 1
        if civ[0] == 1:
            if civnotnot[1] == 0:
                civ[0] = civnot[1]
                civnotnot[1] = 1
                civdonnum = 1
        if civ[0] == 2:
            if civnotnot[2] == 0:
                civ[0] = civnot[2]
                civnotnot[2] = 1
                civdonnum = 1
        if civ[0] == 3:
            if civnotnot[3] == 0:
                civ[0] = civnot[3]
                civnotnot[3] = 1
                civdonnum = 1
        if civ[0] == 4:
            if civnotnot[4] == 0:
                civ[0] = civnot[4]
                civnotnot[4] = 1
                civdonnum = 1
        if civdonnum == 1:
            print("La primera civilización es: " , civ[0] )
    print("Eligiendo segunda civilización")
    while civdonnum == 1:
        civ[1] = randint (0,4)
        if civ[1] == 0:
            if civnotnot[0] == 0:
                civ[1] = civnot[0]
                civnotnot[0] = 1
                civdonnum = 2
        if civ[1] == 1:
            if civnotnot[1] == 0:
                civ[1] = civnot[1]
                civnotnot[1] = 1
                civdonnum = 2
        if civ[1] == 2:
            if civnotnot[2] == 0:
                civ[1] = civnot[2]
                civnotnot[2] = 1
                civdonnum = 2
        if civ[1] == 3:
            if civnotnot[3] == 0:
                civ[1] = civnot[3]
                civnotnot[3] = 1
                civdonnum = 2
        if civ[1] == 4:
            if civnotnot[4] == 0:
                civ[1] = civnot[4]
                civnotnot[4] = 1
                civdonnum = 2
        if civdonnum == 2:
            print("La segunda civilización es: " , civ[1])
    print("Eligiendo tercera civilización")
    while civdonnum == 2:
        civ[2] = randint (0,4)
        if civ[2] == 0:
            if civnotnot[0] == 0:
                civ[2] = civnot[0]
                civnotnot[0] = 1
                civdonnum = 3
        if civ[2] == 1:
            if civnotnot[1] == 0:
                civ[2] = civnot[1]
                civnotnot[1] = 1
                civdonnum = 3
        if civ[2] == 2:
            if civnotnot[2] == 0:
                civ[2] = civnot[2]
                civnotnot[2] = 1
                civdonnum = 3
        if civ[2] == 3:
            if civnotnot[3] == 0:
                civ[2] = civnot[3]
                civnotnot[3] = 1
                civdonnum = 3
        if civ[2] == 4:
            if civnotnot[4] == 0:
                civ[2] = civnot[4]
                civnotnot[4] = 1
                civdonnum = 3
        if civdonnum == 3:
                print("La tercera civilización es: " , civ[2])
    print("Eligiendo cuarta civilización")
    while civdonnum == 3:
        civ[3] = randint (0,4)
        if civ[3] == 0:
            if civnotnot[0] == 0:
                civ[3] = civnot[0]
                civnotnot[0] = 1
                civdonnum = 4
        if civ[3] == 1:
            if civnotnot[1] == 0:
                civ[3] = civnot[1]
                civnotnot[1] = 1
                civdonnum = 4
        if civ[3] == 2:
            if civnotnot[2] == 0:
                civ[3] = civnot[2]
                civnotnot[2] = 1
                civdonnum = 4
        if civ[3] == 3:
            if civnotnot[3] == 0:
                civ[3] = civnot[3]
                civnotnot[3] = 1
                civdonnum = 4
        if civ[3] == 4:
            if civnotnot[4] == 0:
                civ[3] = civnot[4]
                civnotnot[4] = 1
                civdonnum = 4
        if civdonnum == 4:
                print("La cuarta civilización es: " , civ[3])
    print("Eligiendo quinta civilización")
    while civdonnum == 4:
            civ[4] = randint (0,4)
            if civ[4] == 0:
                if civnotnot[0] == 0:
                    civ[4] = civnot[0]
                    civnotnot[0] = 1
                    civdonnum = 5
            if civ[4] == 1:
                if civnotnot[1] == 0:
                    civ[4] = civnot[1]
                    civnotnot[1] = 1
                    civdonnum = 5
            if civ[4] == 2:
                if civnotnot[2] == 0:
                    civ[4] = civnot[2]
                    civnotnot[2] = 1
                    civdonnum = 5
            if civ[4] == 3:
                if civnotnot[3] == 0:
                    civ[4] = civnot[3]
                    civnotnot[3] = 1
                    civdonnum = 5
            if civ[4] == 4:
                if civnotnot[4] == 0:
                    civ[4] = civnot[4]
                    civnotnot[4] = 1
                    civdonnum = 5
            if civdonnum == 5:
                    print("La quinta civilización es: " , civ[4])
                    reparto = 1
print("Civilizalaciones disponibles: Grecia, Roma, Egipto, Arabia, Mesopotamia (a fecha de 22/09).")
print("Repartiendo civilizaciones en zonas")
