# -*- coding: utf-8 -*-
while True:
    n,m = map(int,input().split())
    if n == m == 0:
        break
    lista = []
    total = 4
    for i in range(n):
        lista.append([int(x) for x in input().split()])

    for i in range(n):
        p = lista[i].count(1)
        if p==m:
            total -= 1
            break

    problema = [0] * m
    for i in range(n):
        for j in range(m):
            if lista[i][j] == 1:
                problema[j] += 1
    if problema.count(0) > 0:
        total -= 1

    for j in range(m):
        if problema[j] == n:
            total -= 1
            break

    for i in range(n):
        p = lista[i].count(0)
        if p==m:
            total -= 1
            break
    print(total)