# -*- coding: utf-8 -*-
while True:
    lista = []
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    else:
        if m > n:
            m, n = n, m
        for i in range(m, n+1):
            lista.append(i)
        s = "Sum=%d"%sum(lista)
        lista.append(s)
        print(" ".join(map(str,lista)))
