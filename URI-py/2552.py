# -*- coding: utf-8 -*-
while True:
    try:
        lista = []
        n,m = map(int,input().split())
        for i in range(n):
            lista.append([int(x) for x in input().split()])
        mat = [None] * n
        for i in range(n):
            mat[i] = [None] * m
        for i in range(len(lista)):
            for u in range(m):
                if lista[i][u] == 1:
                    mat[i][u] = 9
                else:
                    mat[i][u] = 0
        for i in range(n):
            for u in range(m-1):
                cont = 0
                if i != n-1 and u != m-1:
                    if mat[i][u] == 0:
                        if mat[i+1][u] == 9:
                            cont += 1
                        if mat[i][u+1] == 9:
                            cont += 1

            print(mat[i])
    except EOFError:
        break

'''
                    if mat[i+1][u] == 9:
                        cont += 1
                    if mat[i-1][u] == 9:
                        cont += 1
                    if mat[i][u+1] == 9:
                        cont += 1
                    if mat[i][u-1] == 9:
                        cont += 1
'''