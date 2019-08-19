# -*- coding: utf-8 -*-
n = int(input())
lista = list(map(int,input().split()))
pos = cont = 0
menor = lista[0]
for i in lista:
    if i<menor:
        menor = i
        pos = cont
    cont += 1
print("Menor valor: %d"%menor)
print("Posicao: %d"%pos)
