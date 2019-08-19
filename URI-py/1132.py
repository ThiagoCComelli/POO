# -*- coding: utf-8 -*-
x = int(input())
y = int(input())
soma = 0
if x > y:
    for i in range(y, x + 1):
        if (i % 13) != 0:
            soma += i
if y > x:
    for i in range(x, y + 1):
        if (i % 13) != 0:
            soma += i
print(soma)
