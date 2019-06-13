# -*- coding: utf-8 -*-
pos = 0
for i in range (10):
    n = int(input())
    if (n < 0) or n == 0:
        print("X[%d] = 1"%pos)
    else:
        print("X[%d] = %d"%(pos,n))
    pos += 1
