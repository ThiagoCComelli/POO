# -*- coding: utf-8 -*-
qtde = 0
nota = 0
while qtde < 2:
    x = float(input())
    if x >= 0 and x <= 10:
        nota += x
        qtde += 1
    else:
        print("nota invalida")
print("media = %.2f"%(nota/2))
