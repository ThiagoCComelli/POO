# -*- coding: utf-8 -*-
n = int(input())
lista = []
s = 0
for i in range(n):
    v = input()
    va1, va2 = map(int,input().split())
    lista.append(v)
    s = va1 + va2
    if (s%2)==0:
        print(lista[0])
    elif (s%2)!=0:
        print(lista[2])
