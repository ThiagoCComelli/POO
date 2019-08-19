# -*- coding: utf-8 -*-
import math
while True:
    n = int(input())
    if n == 0:
        break
    mat = [None] * n
    for i in range(n):
        mat[i] = [None]*n
    x = 1
    maior = 0
    c = 0
    for i in range(n):
        for j in range(n):
            mat[i][j] = 2**(i+j)
            c = mat[i][j] = 2**(i+j)
            if c > maior:
                maior = c
    for i in mat:
        print('{:{}}'.format(i,len(str(maior))))

