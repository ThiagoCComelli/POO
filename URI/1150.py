# -*- coding: utf-8 -*-
x = int(input())
y = 0
while True:
    y = int(input())
    if y > x:
        break
soma = x
q = 1
while soma<y:
    soma += x+q
    q += 1
print(q)
