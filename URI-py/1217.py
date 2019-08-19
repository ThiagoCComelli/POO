# -*- coding: utf-8 -*-
n = int(input())
dia = 1
s = 0
c = 0
for i in range(n):
    pre = float(input())
    s += pre
    comidas = input()
    comidas = comidas.split()
    c += len(comidas)
    print("day %d: %d kg"%(dia,int(len(comidas))))
    dia += 1
print("%.2f kg by day"%(c/n))
print("R$ %.2f by day"%(s/n))
