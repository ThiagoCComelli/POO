# -*- coding: utf-8 -*-
n,m = [int(x) for x in input().split()]
lista = [0] * n
for i in range(m):
    p, d = map(int,input().split())
    lista[p-1] = 1
    if p-d < n:
        lista[i] = 1

print(lista)
