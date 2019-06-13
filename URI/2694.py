# -*- coding: utf-8 -*-
n = int(input())
for i in range(n):
    f = str(input())
    s = 0
    lista = []
    for o in f:
        if o.isdecimal():
            s += int(o)
    print(s)
