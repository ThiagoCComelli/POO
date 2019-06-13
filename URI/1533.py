# -*- coding: utf-8 -*-
while True:
    n = int(input())
    if n == 0:
        break
    else:
        qtde = input().split()
        for i in range(n):
            qtde[i] = int(qtde[i])
        sor = sorted(qtde, key=int)
        a = sor[-2]
        for pos, valor in enumerate(qtde, 1):
            if valor == a:
                print(pos)
