# -*- coding: utf-8 -*-
n = int(input())
lista1 = []
for i in range(n):
    lista = []
    frase = str(input())
    for u in frase:
        if u == u.lower():
            lista.append(u)
    lista = lista[::-1]
    lista1.append(lista)
for o in lista1:
    print(*o,sep="")

