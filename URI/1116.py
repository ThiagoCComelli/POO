# -*- coding: utf-8 -*-
n = int(input())
contador = 0
while contador<n:
    x, y = map(int, input().split())
    if y==0:
        print("divisao impossivel")
    else:
        c = x/y
        print("%.1f"%c)
    contador += 1
