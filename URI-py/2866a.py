# -*- coding: utf-8 -*-
n = int(input())
for i in range(n):
    frase = str(input())
    lista = []
    for u in frase:
        if u == u.lower():
            lista.append(u)
    print(*lista[::-1],sep="")
