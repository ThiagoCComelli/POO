# -*- coding: utf-8 -*-
n = int(input())
d = 0
f = 0
for i in range(n):
    n1 = int(input())
    if 10<=n1<21:
        d += 1
    else:
        f += 1
print("%d in\n%d out"%(d,f))
