# -*- coding: utf-8 -*-
while True:
    try:
        n = int(input())
        lista = []
        for i in range(n):
            lista.append(input())
        for u in sorted(lista):
            print(u)
    except EOFError:
        break
