# -*- coding: utf-8 -*-
n = int(input())
for i in range(n):
    def mdc(a,b):
        resto = None
        while resto is not 0:
            resto = b%a
            b = a
            a = resto
        return b
    a,b = input().split()
    a = int(a)
    b = int(b)
    print(mdc(a,b))
