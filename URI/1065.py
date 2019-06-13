# -*- coding: utf-8 -*-
pares = 0
lista = []
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
for i in lista:
    if (i%2)==0:
        pares += 1
print("%d valores pares"%pares)
