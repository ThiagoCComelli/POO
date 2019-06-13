# -*- coding: utf-8 -*-
lista = []
lista1 = []
n,m = map(int,input().split())
for i in range(n):
    lista.append([int(x) for x in input().split()])
for i in range(n):
    t = 0
    for j in range(m):
        t += lista[i][j]
    lista1.append(t)
for j in range(m):
    t = 0
    for i in range(n):
        t += lista[i][j]
    lista1.append(t)
print(max(lista1))