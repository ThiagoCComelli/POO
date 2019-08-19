# -*- coding: utf-8 -*-
lista = []
for i in range(99):
    n = float(input())
    lista.append(n)
for i in range(99):
    if lista[i]<=10:
        print("A[%d] = %.1f"%(i,lista[i]))
