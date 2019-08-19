# -*- coding: utf-8 -*-
v = int(input())
va = map(int,input().split())
lista = []
for i in va:
    lista.append(i)
print(sum(lista)-v)
