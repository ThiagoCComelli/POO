# -*- coding: utf-8 -*-
while True:
    try:
        n,m = [int(x) for x in input().split()]
        lista = []
        a = b = c = d =0
        for i in range(n):
            lista.append([int(x) for x in input().split()])
        for i in range(n):
            for j in range(m):
                if lista[i][j] == 1:
                    a += i+1
                    c += j+1
                if lista[i][j] == 2:
                    b += i+1
                    d += j+1
        print(abs(a-b)+abs(c-d))
    except EOFError:
        break
