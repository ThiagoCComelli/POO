# -*- coding: utf-8 -*-
while True:
    try:
        s = 0
        n = int(input())
        lista = []
        listad = []
        listae = []
        for i in range(n):
            valor = input()
            valor = str(valor)
            lista.append(valor)
        for p in lista:
            if p[3] == "D":
                listad.append(p[0:2])
            if p[3] == "E":
                listae.append(p[0:2])
        for u in listae:
            if u in listad:
                s += 1
                listad.remove(u)
        print(s)
    except EOFError:
        break
