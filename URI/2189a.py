# -*- coding: utf-8 -*-
t = 1
while True:
    n = int(input())
    if n == 0:
        break
    lista = [int(i) for i in input().split()]
    ven = [lista[i] for i in range(n) if lista[i] == (i+1)]
    print("Teste %d"%(t))
    print(ven[0],end="\n\n")
    t+=1
