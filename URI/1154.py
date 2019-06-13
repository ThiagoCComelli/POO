# -*- coding: utf-8 -*-
qtde = 0
soma = 0
while True:
    n = int(input())
    if n >= 0:
        soma += n
        qtde += 1
    else:
        break
print("%.2f"%(soma/qtde))
