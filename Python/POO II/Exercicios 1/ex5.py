# -*- coding: utf-8 -*-
n = int(input())
prod = 0
for i in range(1,n):
    if i == 1:
        prod += i
    else:
        prod *= i
print(prod)

