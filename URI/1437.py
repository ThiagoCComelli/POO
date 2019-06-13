# -*- coding: utf-8 -*-
while True:
    lista = []
    n = int(input())
    if n == 0:
        break
    direcao = str(input())
    for i in direcao:
        lista.append(i)
    s = 0
    s += lista.count("D")
    s -= lista.count("E")
    d = s % 4
    if d == 0:
        print("N")
    elif d == 1:
        print("L")
    elif d == 2:
        print("S")
    elif d == 3:
        print("O")

