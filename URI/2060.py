# -*- coding: utf-8 -*-
n = int(input())
v = map(int,input().split())
lista = []
m2 = 0
m3 = 0
m4 = 0
m5 = 0
for i in v:
    lista.append(i)
    if (i%2)==0:
        m2 += 1
    if (i%3)==0:
        m3 += 1
    if (i%4)==0:
        m4 += 1
    if (i%5)==0:
        m5 += 1
print("%d Multiplo(s) de 2"%m2)
print("%d Multiplo(s) de 3"%m3)
print("%d Multiplo(s) de 4"%m4)
print("%d Multiplo(s) de 5"%m5)
