# -*- coding: utf-8 -*-
n = int(input())
ins = 1
lista = {}

while True:
    try:
        for i in range(n):
            f = input().split()
            lista[int(f[1])] = f[0]
        print("Instancia {}".format(ins))
        print(lista[min(lista)])
        ins += 1
    except EOFError:
        break