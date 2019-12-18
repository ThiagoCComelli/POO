# -*- coding: utf-8 -*-
min = 2
max = 100000
for i in range(min,max):
    for u in range(2, i):
        if (i % u) == 0:
            break
    else:
        print(i)