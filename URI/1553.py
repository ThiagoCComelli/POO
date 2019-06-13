# -*- coding: utf-8 -*-
while True:
    n, k = map(int,input().split())
    lista = input().split()
    s = 0
    if n == 0 and k == 0:
        break
    elif n != 0 and k != 0:
        for i in range(n):
            lista[i] = int(lista[i])
        for u in lista:
            if lista.count(u)>=k:
                s += 1
                while u in lista:
                    lista.remove(u)
    print(s)
