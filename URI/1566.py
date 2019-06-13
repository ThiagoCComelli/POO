# -*- coding: utf-8 -*-
for i in range(int(input())):
    lista = []
    n = int(input())
    lista.append([int(x) for x in input().split()])
    for i in lista:
        i.sort()
        print(*i)