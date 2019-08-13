# -*- coding: utf-8 -*-
qtde = 0
val = 0
while True:
    n = float(input())
    val += n
    if n == 0:
        break
    qtde += 1
print(val/qtde)