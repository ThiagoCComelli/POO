# -*- coding: utf-8 -*-
p, d = map(int,input().split())
postos = [int(i) for i in input().split()]
s = 0
f = 0
lista = []
for i in range(p):
    lista.append(s)
    s += d
for o in range(p):
    if postos[o]>lista[o]:
        f += 1
if f != 0:
    print("N")
else:
    if (max(postos)+d) <= 42194:
        print("N")
    else:
        print("S")
