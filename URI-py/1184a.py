# -*- coding: utf-8 -*-
o = input()
soma = 0
qtde = 0
for i in range(12):
    for j in range(12):
        n = float(input())
        if i > j:
            soma += n
            qtde += 1
if o == "S":
    print("%.1f"%soma)
else:
    print("%.1f"%(soma/qtde))

