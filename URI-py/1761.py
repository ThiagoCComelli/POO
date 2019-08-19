# -*- coding: utf-8 -*-
import math
while True:
    try:
        pi = 3.141592654
        n = [float(i) for i in input().split()]
        print('{:.2f}'.format(5*(math.tan(pi*n[0]/180)*n[1]+n[2])))
    except EOFError:
        break