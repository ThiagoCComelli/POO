# -*- coding: utf-8 -*-
i, j = 1, 7
while i < 10:
    print("I=%d J=%d"%(i,j))
    j -= 1
    if j < 5:
        j = 7
        i += 2
