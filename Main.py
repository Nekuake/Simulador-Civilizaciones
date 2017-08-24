#!/usr/bin/env python
# -*- codcivdoning: utf-8 -*-
from random import randint                      #Para la aleatoriedad
civtemp= 0
reparto = 0                                     #Variable que determina si la generación inicial ha terminado y se puede salir del while (lin= )
civdon = [0,0,0,0,0]
civdonnum = 0                                   #Variable que muestra en que lugar de las 5 civilizaciones se encuentra la generación
civ = [0,0,0,0,0]
pobciv = [0,0,0,0,0]
zona = ["Mediterráneo","Oriente Próximo","Europa Oeste","Europa Este","Norte de Asia","Australia","Asia Este","Sudamérica","Norteamérica"]
civnot = ["Arabia","Grecia","Roma","Egipto","Mesopotamia"]
civnotnot = [0,0,0,0,0]
from funciones import repartofuncion
print("Generando civilizaciones en sus lugares.")
civ[0] = repartofuncion()
civ[1] = repartofuncion()
civ[2] = repartofuncion()
civ[3] = repartofuncion()
civ[4] = repartofuncion()
print("La primera civilización es", civ[0])
print("La segunda civilización es", civ[1])
print("La tercera civilización es", civ[2])
print("La cuarta civilización es", civ[3])
print("La quinta civilización es", civ[4])
print("Civilizalaciones disponibles: Grecia, Roma, Egipto, Arabia, Mesopotamia (a fecha de 22/09).")
print("Repartiendo civilizaciones en zonas")
