# -*- coding: utf-8 -*-
n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    nrs = input().split()
    for o in range(a):
        nrs[o] = int(nrs[o])
    if nrs.count(b) >= 1:
        for pos, valor in enumerate(nrs, 1):
            if b == valor:
                print(pos)
                break
    else:
        x = min(nrs,key=lambda x:abs(x-b))
        print((nrs.index(x))+1)


