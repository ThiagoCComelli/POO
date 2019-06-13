# -*- coding: utf-8 -*-
while True:
    try:
        n,m = [int(x) for x in input().split()]
        lista = []
        a = 0
        b = 0
        lista1 = []
        lista2 = []
        lista3 = []
        for i in range(n):
            lista.append([int(x) for x in input().split()])
        for i in range(len(lista)):
            for j in lista[i]:
                if j == 1:
                    lista1.append(lista[i].index(j)+1)
                    lista2.append(i+1)
                if j == 2:
                    lista1.append(lista[i].index(j)+1)
                    lista2.append(i+1)
        print(lista1)
        print(lista2)
        for a, b in zip(lista1,lista2):
            lista3.append(a+b)
        print(abs(lista3[0]-lista3[1]))
    except EOFError:
        break
