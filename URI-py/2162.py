# -*- coding: utf-8 -*-
n = int(input())
hs = input().split()
for i in range(0,n):
    hs[i] = int(hs[i])
padrao = 1
forma = 0
for i in range(1,n):
    if hs[i] < hs[i-1]:
        if forma == 1:
            padrao = 0
            break
        else:
            forma = 1
    elif hs[i] > hs[i-1]:
        if forma == 2:
            padrao = 0
            break
        else:
            forma = 2
    else:
        padrao = 0
        break
print(padrao)
