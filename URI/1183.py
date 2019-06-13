# -*- coding: utf-8 -*-
O = input()

mat = [None] * 12
for i in range(0,12):
    mat[i]= [None] * 12

for i in range(0,12):
    for j in range(0,12):
        mat[i][j] = float(input())

soma = 0
qtde = (144-12)/2
for i in range(0,12):
    for j in range(i+1,12):
        soma += mat[i][j]

if O == "S":
    print("%.1f"%soma)
else:
    print("%.1f"%(soma/qtde))
