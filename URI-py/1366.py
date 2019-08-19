# -*- coding: utf-8 -*-
while True:
    n = int(input())
    lista = []
    lista2 = 0
    if n == 0:
        break
    else:
        for i in range(n):
            c, v = map(int,input().split())
            for o in range(v):
                lista.append(c)
        for u in set(lista):
            if lista.count(u)>=2:
                lista2 += int(lista.count(u)//2)
        print(int(lista2/2))
