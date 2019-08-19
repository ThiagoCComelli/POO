# -*- coding: utf-8 -*-
while True:
    lista = []
    #list.clear(lista)
    x = int(input())
    if x == 0:
        break
    for i in range(1,x+1):
        lista.append(i)
    print(" ".join(map(str, lista)))
