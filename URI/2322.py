# -*- coding: utf-8 -*-
n = int(input())
n1 = [int(x) for x in input().split()]
c = True
maior = max(n1)
for i in range(n,0,-1):
    if i not in n1:
        print(i)
