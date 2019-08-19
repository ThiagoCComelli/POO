# -*- coding: utf-8 -*-
c, v = map(int,input().split())
lista = []
for i in range(c):
    tempo = map(int,input().split())
    lista.append(sum(tempo))
print((lista.index(min(lista)))+1)
