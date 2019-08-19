# -*- coding: utf-8 -*-
a, b, c = map(float, input().split())
tri = (b-c)
per = (a+b+c)
if tri < a < (b+c):
    per = (a+b+c)
    print("Perimetro = %.1f"%per)
else:
    a = ((a+b)*c)/2
    print("Area = %.1f"%a)
