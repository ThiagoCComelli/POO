# -*- coding: utf-8 -*-
ins = 0
lista = []
while True:
    a = float(input())
    b = float(input())
    print("(1) Adicao | (2) Subtracao | (3) Multiplicacao | (4) Divisao | (5) Saida")
    op = int(input())
    if op == 1:
        lista.append(a+b)
    elif op == 2:
        lista.append(a-b)
    elif op == 3:
        lista.append(a*b)
    elif op == 4:
        lista.append(a/b)
    elif op == 5:
        for i in lista:
            print("Instancia: {} | Saida: {}".format(ins,i))
            ins += 1
        break