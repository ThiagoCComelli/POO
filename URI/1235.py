# -*- coding: utf-8 -*-
n = int(input())
for i in range(n):
    frase = input()
    t = len(frase)
    lista = []
    metade = len(frase)-len(frase)//2
    lista.append((frase[0:metade][::-1]))
    lista.append((frase[metade:][::-1]))
    print(*lista,sep="")
