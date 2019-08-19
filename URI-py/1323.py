# -*- coding: utf-8 -*-
poss = [0]
for i in range(1, 101):
    poss.append(i * i + poss[i - 1])

while (True):
    n = int(input())
    if (n == 0):
        break
    print(poss[n])
