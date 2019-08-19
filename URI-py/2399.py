# -*- coding: utf-8 -*-
lista = []
n = int(input())
for i in range(n):
    lista.append(int(input()))
for i in range(n):
    t = 0
    if i == 0:
        if lista[i] == 1:
            t += 1
            if lista[i+1] == 1:
                t += 1
        elif lista[i] == 0:
            if lista[i + 1] == 1:
                t += 1
        print(t)
    elif i == n-1:
        if lista[i] == 1:
            t += 1
            if lista[i-1] == 1:
                t += 1
        elif lista[i] == 0:
            if lista[i-1] == 1:
                t += 1
        print(t)
    else:
        if lista[i] == 0:
            if lista[i+1] == 1:
                t += 1
            if lista[i-1] == 1:
                t += 1
            print(t)
        elif lista[i] == 1:
            t += 1
            if lista[i+1] == 1:
                t += 1
            if lista[i-1] == 1:
                t += 1
            print(t)

