# -*- coding: utf-8 -*-
n,m = map(int,input().split())
t = 0
for i in range(n):
    p = input().split()
    if p.count("0") == 0:
        t += 1
print(t)

