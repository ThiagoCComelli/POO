# -*- coding: utf-8 -*-
while True:
    s = 0
    qtde = 0
    while qtde < 2:
        n = float(input())
        if n<=10 and n>=0:
            s += n
            qtde += 1
        else:
            print("nota invalida")
    print("media = %.2f"%(s/2))
    denovo = 0
    while True:
        print("novo calculo (1-sim 2-nao)")
        denovo = int(input())
        if denovo==1 or denovo==2:
            break
    if denovo==2:
        break
