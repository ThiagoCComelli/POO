# -*- coding: utf-8 -*-
o = input()

mat = [None] * 12
for i in range(0,12):
    mat[i] = [None] * 12

for i in range(0,12):
    for j in range(0,12):
        mat[i][j] = float(input())

soma = 0
qtde = (144-24)/4

for i in range(0,6):
    for j in range(0,i):
        soma += mat[i][j]

for i in range(6,12):
    for j in range(0,12-1-1):
        soma += mat[i][j]

if o == "S":
    print("%.1f"%soma)
else:
    print("%.1f"%(soma/qtde))
