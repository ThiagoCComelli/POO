# -*- coding: utf-8 -*-
positivos = 0
soma = 0
lista= []
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))

for i in lista:
    if i>0:
        positivos += 1
        soma += i
print("%d valores positivos\n%.1f"%(positivos,(soma/positivos)))
