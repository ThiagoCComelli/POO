# -*- coding: utf-8 -*-
qtde = int(input())
lista = input().split()
padrao = 0
while len(lista)>qtde:
    lista = lista[:-1]
if lista.count("1")>lista.count("0"):
    print("N")
elif lista.count("1")==lista.count("0"):
    print("N")
elif lista.count("1")<lista.count("0"):
    print("Y")

