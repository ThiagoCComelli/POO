# -*- coding: utf-8 -*-
a, b, c = map(int,input().split())
if a > 0 and b > 0 and c > 0:
    if abs(b-c)<a<(b+c):
        if a != b and a != c and b != c:
            print("Valido-Escaleno")
        elif a == b and b == c and c == a:
            print("Valido-Equilatero")
        elif a == b or b == c or a == c:
                print("Valido-Isoceles")
        if (a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2):
            print('Retangulo: S')
        else:
            print('Retangulo: N')
    else:
        print("Invalido")


