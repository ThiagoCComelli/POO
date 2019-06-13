# -*- coding: utf-8 -*-
n = int(input())
q = 0
n1 = 0
for i in range(1000):
    print("N[%d] = %d"%(q,n1))
    q += 1
    n1 += 1
    if n1 == n:
        n1 = 0
