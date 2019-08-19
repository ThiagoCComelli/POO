# -*- coding: utf-8 -*-
while True:
    try:
        x,y = map(int, input().split())
        lista = []
        for i in range(x):
            lista.append(int(input()))
        lista.sort(reverse=True)
        for i in range(y):
            pos = int(input())
            print(lista[pos-1])
    except EOFError:
        break