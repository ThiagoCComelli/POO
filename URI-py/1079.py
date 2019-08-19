# -*- coding: utf-8 -*-
n = int(input())
for _ in range(n):
    lista = list(map(float, input().split()))
    no1, no2, no3 = lista
    no1 = no1*2
    no2 = no2*3
    no3 = no3*5
    m = (no1+no2+no3)/10
    print("%.1f"%m)
