# -*- coding: utf-8 -*-
n = int(input())
v = n
for _ in range(n):
    n -= 1
    v *= n
    if n==1:
        break
print(v)
