# -*- coding: utf-8 -*-
import math
while True:
    try:
        d, vf, vg = map(int,input().split())
        h = math.sqrt((12**2)+(d**2))
        tempf = 12/vf
        tempg = h/vg
        if tempf<tempg:
            print("N")
        else:
            print("S")
    except EOFError:
        break
