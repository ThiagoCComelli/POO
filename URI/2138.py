# -*- coding: utf-8 -*-
while True:
    try:
        nu = input()
        lista = [0] * 10
        lista1 = []
        for i in nu:
            lista[int(i)] += 1
        a = set(lista)
        print(9-lista[::-1].index(max(lista)))
    except EOFError:
        break
