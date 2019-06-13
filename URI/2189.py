# -*- coding: utf-8 -*-
t = 1
while True:
    n = int(input())
    p = 1
    if n == 0:
        break
    lista = input().split()
    for i in range(n):
        lista[i] = int(lista[i])
    for o in lista:
        if o != p:
            p += 1
        else:
            print("Teste %d"%t)
            print(p,end="\n\n")
            t += 1
