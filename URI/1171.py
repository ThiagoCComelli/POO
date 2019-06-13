# -*- coding: utf-8 -*-
n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
lista1 = lista
lista = set(lista)
for i in sorted(lista):
    print("{} aparece {} vez(es)".format(i,lista1.count(i)))