# -*- coding: utf-8 -*-
# l = largura
# A = altura
# P = profundidade
# R = raio
l, a, p, r = map(int, input().split())
dia = ((l**2)+(a**2)+(p**2))**(1/2)
if ((l**2)+(a**2)+(p**2)) <= (4*(r**2)):
    print("S")
else:
    print("N")
