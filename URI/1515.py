# -*- coding: utf-8 -*-
while True:
    lista = []
    lista1 = []
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        dados = input().split()
        lista1.append(str(dados[0]))
        lista.append(int(dados[1])-(int(dados[2])))
        a = lista.index(min(lista))
    print(lista1[a])
