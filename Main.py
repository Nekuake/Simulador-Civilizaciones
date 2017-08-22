#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint                      #Para la aleatoriedad
civdon = 0                                      #Variable que determina si la generación inicial ha terminado y se puede salir del while (lin= )
civdon0 = 0
cindon1 = 0
civdon2 = 0
civdon3 = 0
civdon4 = 0
civdonnum = 0                                   #Variable que muestra en que lugar de las 5 civilizaciones se encuentra la generación
civ0 = 0                                        #Civilizalaciones que entrarán
civ1 = 0
civ2 = 0
civ3 = 0
civ4 = 0
pobciv0 = 0
pobciv1 = 0
pobciv2 = 0
pobciv3 = 0
pobciv4 = 0
zona0 = "Mediterráneo"                          #Zonas donde están las civilizaciones
zona1 = "Oriente Próximo"
zona2 = "Europa Oeste"
zona3 = "Europa Este"
zona4 = "Norte de Asia"
zona5 = "Australia"
zona6 = "Asia Este"
zona7 = "Sudamérica"
zona8 = "Norteamérica"
civnot0 = "Arabia"                              #Civilizaciones sin entrar todavia
civnot1 = "Grecia"
civnot2 = "Roma"
civnot3 = "Egipto"
civnot4 = "Mesopotamia"
civnot0not = 0                                  #Variable que determina si una civilización ha entrado o no ya
civnot1not = 0
civnot2not = 0
civnot3not = 0
civnot4not = 0
print("Generando civilizaciones en sus lugares.")
while civdon != 1:
    while civdonnum == 0:
        print("Eligiendo primera civilización")
        civ0 = randint (0,4)
        if civ0 == 0:
            if civnot0not == 0:
                civ0 = civnot0
                civnot0not = 1
                civdonnum = 1
        if civ0 == 1:
            if civnot1not == 0:
                civ0 = civnot1
                civnot1not = 1
                civdonnum = 1
        if civ0 == 2:
            if civnot2not == 0:
                civ0 = civnot2
                civnot2not = 1
                civdonnum = 1
        if civ0 == 3:
            if civnot3not == 0:
                civ0 = civnot3
                civnot3not = 1
                civdonnum = 1
        if civ0 == 4:
            if civnot4not == 0:
                civ0 = civnot4
                civnot4not = 1
                civdonnum = 1
        if civdonnum == 1:
            print("La primera civilización es: " , civ0 )
    while civdonnum == 1:
        print("Eligiendo segunda civilización")
        civ1 = randint (0,4)
        if civ1 == 0:
            if civnot0not == 0:
                civ1 = civnot0
                civnot0not = 1
                civdonnum = 2
        if civ1 == 1:
            if civnot1not == 0:
                civ1 = civnot1
                civnot1not = 1
                civdonnum = 2
        if civ1 == 2:
            if civnot2not == 0:
                civ1 = civnot2
                civnot2not = 1
                civdonnum = 2
        if civ1 == 3:
            if civnot3not == 0:
                civ1 = civnot3
                civnot3not = 1
                civdonnum = 2
        if civ1 == 4:
            if civnot4not == 0:
                civ1 = civnot4
                civnot4not = 1
                civdonnum = 2
        if civdonnum == 2:
            print("La segunda civilización es: " , civ1)
    while civdonnum == 2:
        print("Eligiendo tercera civilización")
        civ2 = randint (0,4)
        if civ2 == 0:
            if civnot0not == 0:
                civ2 = civnot0
                civnot0not = 1
                civdonnum = 3
        if civ2 == 1:
            if civnot1not == 0:
                civ2 = civnot1
                civnot1not = 1
                civdonnum = 3
        if civ2 == 2:
            if civnot2not == 0:
                civ2 = civnot2
                civnot2not = 1
                civdonnum = 3
        if civ2 == 3:
            if civnot3not == 0:
                civ2 = civnot3
                civnot3not = 1
                civdonnum = 3
        if civ2 == 4:
            if civnot4not == 0:
                civ2 = civnot4
                civnot4not = 1
                civdonnum = 3
        if civdonnum == 3:
                print("La tercera civilización es: " , civ2)
    while civdonnum == 3:
        print("Eligiendo cuarta civilización")
        civ3 = randint (0,4)
        if civ3 == 0:
            if civnot0not == 0:
                civ3 = civnot0
                civnot0not = 1
                civdonnum = 4
        if civ3 == 1:
            if civnot1not == 0:
                civ3 = civnot1
                civnot1not = 1
                civdonnum = 4
        if civ3 == 2:
            if civnot2not == 0:
                civ3 = civnot2
                civnot2not = 1
                civdonnum = 4
        if civ3 == 3:
            if civnot3not == 0:
                civ3 = civnot3
                civnot3not = 1
                civdonnum = 4
        if civ3 == 4:
            if civnot4not == 0:
                civ3 = civnot4
                civnot4not = 1
                civdonnum = 4
        if civdonnum == 4:
                print("La cuarta civilización es: " , civ3)
        while civdonnum == 4:
            print("Eligiendo quinta civilización")
            civ3 = randint (0,4)
            if civ4 == 0:
                if civnot0not == 0:
                    civ4 = civnot0
                    civnot0not = 1
                    civdonnum = 5
            if civ4 == 1:
                if civnot1not == 0:
                    civ4 = civnot1
                    civnot1not = 1
                    civdonnum = 5
            if civ4 == 2:
                if civnot2not == 0:
                    civ4 = civnot2
                    civnot2not = 1
                    civdonnum = 5
            if civ4 == 3:
                if civnot3not == 0:
                    civ4 = civnot3
                    civnot3not = 1
                    civdonnum = 5
            if civ4 == 4:
                if civnot4not == 0:
                    civ4 = civnot4
                    civnot4not = 1
                    civdonnum = 5
            if civdonnum == 5:
                    print("La quinta civilización es: " , civ4)
                    civdon = 1
print("Civilizalaciones disponibles: Grecia, Roma, Egipto, Arabia, Mesopotamia (a fecha de 22/09).")
