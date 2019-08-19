# -*- coding: utf-8 -*-
while True:
    try:
        n,m = [int(x) for x in input().split()]
        lista = []
        a = 0
        b = 0
        for i in range(n):
            lista.append([int(x) for x in input().split()])
        for i in range(n):
            if lista[i].count(1)==1:
                print(lista[i])
                print(i)
                print(lista[i].index(1))
            if lista[i].count(2)==1:
                print(lista[i])
                print(i)
                print(lista[i].index(2))
    except EOFError:
        break
