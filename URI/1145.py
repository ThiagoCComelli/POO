# -*- coding: utf-8 -*-
x, y = map(int,input().split())
lista = []
for i in range(1,y+1):
    lista.append(i)
while True:
    if len(lista) == 0:
        break
    print(*lista[0:x])
    for i in range(x):
        lista.remove(lista[0])
