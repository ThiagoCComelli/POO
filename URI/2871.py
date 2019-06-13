# -*- coding: utf-8 -*-
while True:
    try:
        n,m = map(int,input().split())
        lista = []
        t = 0
        litros = 0
        sacas = 0
        for i in range(n):
            lista.append([int(x) for x in input().split()])
        for i in range(n):
            for j in range(m):
                t += lista[i][j]
        sacas = t//60
        litros = t-(sacas*60)
        print("{} saca(s) e {} litro(s)".format(sacas,litros))
    except EOFError:
        break