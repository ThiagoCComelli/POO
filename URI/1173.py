# -*- coding: utf-8 -*-
lista = []
pos = 0
n = int(input())
for i in range(0, 10):
    lista.append(n)
    print("N[%d] = %d"%(pos,n))
    pos += 1
    n = 2*n
