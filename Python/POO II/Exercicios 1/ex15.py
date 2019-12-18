# -*- coding: utf-8 -*-
n = int(input())
lista = [0,1]
if n==1:
    lista.remove(1)
elif n==2:
    print(*lista)
else:
    for i in range(n):
        a = lista[-1] + lista[-2]
        lista.append(a)
    print(*lista)