# -*- coding: utf-8 -*-
inst = 1
for o in range(int(input())):
    lista = []
    hor = True
    ver = True
    tre = True
    for u in range(9):
        lista.append([int(x) for x in input().split()])
    for i in range(9):
        chek = []
        for j in range(9):
            chek.append(lista[i][j])
        if len(set(chek)) == len(chek):
            hor = True
        else:
            hor = False
            break
    col = 0
    while col < 9:
        chek = []
        for i in range(9):
            chek.append(lista[i][col])
        col += 1
        if len(set(chek)) == len(chek):
            ver = True
        else:
            ver = False
            break
    um , umm = 0, 3
    dois, doiss = 0, 3
    t = 0
    while t < 3:
        chek = []
        for i in range(um,umm):
            for j in range(dois,doiss):
                chek.append(lista[i][j])
        if len(set(chek)) == len(chek):
            tre = True
        else:
            tre = False
            break
        t += 1
        um += 3
        umm += 3
        dois += 3
        doiss += 3
    if hor == True and ver == True and tre == True:
        print("Instancia {}\nSIM\n".format(inst))
    else:
        print("Instancia {}\nNAO\n".format(inst))
    inst += 1