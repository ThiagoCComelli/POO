# -*- coding: utf-8 -*-
lista = input().split()
padrao = 0
for i in range(5):
    lista[i] = int(lista[i])
for x in range(5):
    if (x < 4):
        if (lista[x] > lista[x + 1]):
            padrao += 1

        elif (lista[x] < lista[x + 1]):
            padrao -= 1
if (padrao == 4):
    print("D")
elif (padrao == -4):
    print("C")
else:
    print("N")
