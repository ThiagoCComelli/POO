# -*- coding: utf-8 -*-
while True:
    try:
        c = 1
        lista = [0,1]
        n = int(input())
        while c < n:
            c += 1
            if len(lista)%2==0:
                lista.append(lista[-1] + lista[-2])
            else:
                lista.append(lista[-1] * lista[-2])
        print(lista[n-1])
    except EOFError:
        break