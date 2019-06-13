# -*- coding: utf-8 -*-
a, b, c, d, e = map(float,input().split())
listaa = [a,b,c,d,e]
lista = sorted(listaa)
s = 0
for i in lista:
    s += i
ss = s - lista[0] - lista[4]
print("%.1f"%ss)
