# -*- coding: utf-8 -*-
while True:
    n = int(input())
    if n == 0:
        break
    mat = [1] * n
    for i in range(n):
        mat[i] = [1] * n
    for i in mat:
        print(*i)
