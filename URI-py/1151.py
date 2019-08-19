# -*- coding: utf-8 -*-
n = int(input())
lista = [0,1]
while True:
    if n == 1:
        print("0")
    elif n == 2:
        print("0 1")
    elif n > 2:
        for i in lista:
            lista.append(i[0]+i[1])
