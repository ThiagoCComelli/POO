# -*- coding: utf-8 -*-
n = float(input())
q = 0
for i in range(100):
    print("N[%d] = %.4f"%(q,n))
    q += 1
    n = n/2
