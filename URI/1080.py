# -*- coding: utf-8 -*-
maiornumero = 0
lista = {}
posicao = 0
while posicao < 100:
    valor = int(input())
    if valor > maiornumero:
        maiornumero = valor
        lista[valor] = posicao
    posicao += 1
print(maiornumero)
print(lista[maiornumero]+1)
