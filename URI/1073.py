# -*- coding: utf-8 -*-
x = int(input())
for i in range(1,x+1):
    while i % 2 == 0:
        i2 = i**2
        print("%d^2 = %d"%(i,i2))
        break

