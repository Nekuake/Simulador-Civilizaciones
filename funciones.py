from random import randint
civnotnot = [0,0,0,0,0]
civnot = ["Arabia","Grecia","Roma","Egipto","Mesopotamia"]
def repartofuncion ():
    global civdon
    global civnot
    global civnotnot
    civdonnum = 0
    while civdonnum != 1:
        civtemp = randint (0,4)
        if civtemp == 0:
            if  civnotnot[0] == 0:
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
                civtemp =  civnot[3]
                civnotnot[3] = 1
                civdonnum = 1
        elif civtemp == 4:
            if civnotnot[4] == 0:
                civtemp = civnot[4]
                civnotnot[4] = 1
                civdonnum = 1
    return civtemp
