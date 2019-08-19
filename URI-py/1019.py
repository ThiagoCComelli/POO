# -*- coding: utf-8 -*-
N = int(input())
h = N//3600
h1 = N%3600
m = h1/60
s = h1%60
print("%d:%d:%d"%(h, m, s))
