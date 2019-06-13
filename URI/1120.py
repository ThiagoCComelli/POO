# -*- coding: utf-8 -*-
while True:
    s = 0
    n = input().split()
    d1 = int(n[0])
    d2 = int(n[0])
    lista = []
    if d1 == 0 and d2 == 0:
        break
    for i in n[1]:
        if i != n[0]:
            lista.append(i)
    print(*lista, sep="")
