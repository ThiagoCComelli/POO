# -*- coding: utf-8 -*-
n = int(input())
for i in range(n):
    n, m = map(int,input().split())
    if n<3 or m<0:
        print("0")
    elif n>2 and m>2:
        t = int(n/3)
        t1 = int(m/3)
        print(t1*t)
