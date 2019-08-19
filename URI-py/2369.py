# -*- coding: utf-8 -*-
d = int(input())
ti = 0
if d > 100:
    d1 = d-100
    total = (7)+(20*1)+(70*2)+(d1*5)
    print(total)
elif 30<d<=100:
    d1 = d-30
    total = (7)+(20*1)+(d1*2)
    print(total)
elif 10<d<=30:
    d1 = d-10
    total = (7)+(d1*1)
    print(total)
elif d<=10:
    ti += 7
    print(ti)

