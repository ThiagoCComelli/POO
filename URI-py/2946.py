# -*- coding: utf-8 -*-
n = str(input())
lista = []
while True:
    try:
        n2 = int(input())
        n3 = int(n,2)
        if n3%n2 == 0:
            lista.append(n2)
    except EOFError:
        break
if len(lista) == 0:
    print('Nenhum')
else:
    stra = ''
    for i in set(lista):
        stra += str(i)
        stra += ' '
    print(stra)