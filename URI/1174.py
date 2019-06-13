# -*- coding: utf-8 -*-
pos = 0
qtde = 1
while True:
    n = float(input())
    if n <= 10:
        print("A[%d] = %.1f"%(pos,n))
    qtde += 1
    pos += 1
    if qtde==100:
        break
