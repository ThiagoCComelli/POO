# -*- coding: utf-8 -*-
qte = 1
while True:
    n = int(input())
    if n == -1:
        break
    else:
        print("Teste %d"%qte)
        qte += 1
        if n == 0:
            print("4")
        elif n > 0:
            vezes = 5+(4**n)
            print("%d\n"%vezes)
