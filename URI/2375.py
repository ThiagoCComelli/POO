# -*- coding: utf-8 -*-
d = int(input())
a, l, p = map(int,input().split())
if a < d or l < d or p < d:
    print("N")
elif a >= d and l >= d and p >= d:
    print("S")
