# -*- coding: utf-8 -*-
lista = []
n = 1
c, v = map(int,input().split())
for i in range(c):
    t = map(int,input().split())
    lista.append(sum(t))
lista1 = lista
sor = sorted(lista1,key=int)
pri = sor[0]
seg = sor[1]
ter = sor[2]
print(lista.index(sor[0])+1)
print(lista.index(sor[1])+1)
print(lista.index(sor[2])+1)

