# -*- coding: utf-8 -*-
n = int(input())
for q in range(n):
    v = int(input())
    soma = 0
    for i in range(1,v):
        if (v%i)==0:
            soma += i
    if soma == v:
        print("%d eh perfeito"%v)
    else:
        print("%d nao eh perfeito"%v)
