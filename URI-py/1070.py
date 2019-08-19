# -*- coding: utf-8 -*-
x = int(input())
qtde = 0
while True:
    if (x%2)!=0:
        qtde += 1
        print(x)
    x += 1
    if qtde==6:
        break
