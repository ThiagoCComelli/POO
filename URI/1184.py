# -*- coding: utf-8 -*-
o = input()

mat = [None] * 12
for i in range(0,12):
    mat[i]= [None] * 12

for i in range(0,12):
    for j in range(0,12):
        mat[i][j] = int(input())

soma = 0
qtde = (144-12)/2
for i in range(1,12):
    for j in range(0,i):
        soma += mat[i][j]

if o == "S":
    print("%.1f"%soma)
else:
    print("%.1f"%(soma/qtde))
