# -*- coding: utf-8 -*-
lista = []
mais = menos = 0
for i in range(int(input())):
    a,b = input().split()
    lista.append(b)
    if a == "+":
        mais += 1
    else:
        menos += 1
for i in sorted(lista):
    print(i)
print("Se comportaram: {} | Nao se comportaram: {}".format(mais,menos))