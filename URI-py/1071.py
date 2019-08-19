# -*- coding: utf-8 -*-
a = int(input())
b = int(input())
soma = 0
for i in range(b+1,a):
    if (i%2!=0):
        soma += i
print(soma)
