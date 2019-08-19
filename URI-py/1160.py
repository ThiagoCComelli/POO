# -*- coding: utf-8 -*-
v = int(input())
for i in range (v):
    pa, pb, g1, g2 = map(float,input().split())
    a = 0
    while pa<=pb:
        pag1 = int((pa*(g1/100)))
        pbg2 = int((pb*(g2/100)))
        a += 1
        pa += pag1
        pb += pbg2
        if a > 100:
            break
    if a>100:
        print("Mais de 1 seculo.")
    else:
        print("%d anos."%a)
