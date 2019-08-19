# -*- coding: utf-8 -*-
valores = input().split()
valores = list(map(float,valores))
A,B,C = sorted(valores)[::-1]
c = True
if(A >= B+C):
    print("NAO FORMA TRIANGULO")
    c = False
if(A**2 == (B**2) + (C**2) and c):
    print("TRIANGULO RETANGULO")
if(A**2 > (B**2) + (C**2) and c):
    print("TRIANGULO OBTUSANGULO")
if(A**2 < (B**2) + (C**2) and c):
    print("TRIANGULO ACUTANGULO")
if(A == B and B == C and c):
    print("TRIANGULO EQUILATERO")
if((A == B or B == C) and not (A == B and B == C) and c):
    print("TRIANGULO ISOSCELES")
