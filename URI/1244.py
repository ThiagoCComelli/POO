# -*- coding: utf-8 -*-
for i in range(int(input())):
    lista = []
    lista.append(input().split())
    for i in lista:
        i.sort(key=len,reverse=True)
        print(*i)