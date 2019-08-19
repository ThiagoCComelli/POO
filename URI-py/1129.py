# -*- coding: utf-8 -*-
while True:
    n = int(input())
    if n == 0:
        break
    for u in range(n):
        s = 0
        n1 = input().split()
        lista = []
        for i in n1:
            i = int(i)
            lista.append(i)
            if i <= 127:
                s += 1
        if s == 1:
            if lista.index(min(lista)) == 0:
                print("A")
            elif lista.index(min(lista)) == 1:
                print("B")
            elif lista.index(min(lista)) == 2:
                print("C")
            elif lista.index(min(lista)) == 3:
                print("D")
            elif lista.index(min(lista)) == 4:
                print("E")
        else:
            print("*")
