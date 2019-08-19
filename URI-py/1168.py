# -*- coding: utf-8 -*-
no = int(input())
for i in range(no):
    s = 0
    numero = input()
    numero = str(numero)
    for i in numero:
        if i == "1":
            s += 2
        if i == "2":
            s += 5
        if i == "3":
            s += 5
        if i == "4":
            s += 4
        if i == "5":
            s += 5
        if i == "6":
            s += 6
        if i == "7":
            s += 3
        if i == "8":
            s += 7
        if i == "9":
            s += 6
        if i == "0":
            s += 6
    print("%d leds"%s)
