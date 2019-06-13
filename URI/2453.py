# -*- coding: utf-8 -*-
frase = input().split()
lista = []
lista1 = []
for i in frase:
    lista1.append(i)
    for o in i:
        if o == "p":
            lista1.remove(o)
print(lista1)

