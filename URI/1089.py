# -*- coding: utf-8 -*-
while True:
    n = int(input())
    if n == 0:
        break
    a = [int(x) for x in input().split()]
    a.append(a[0])
    a.append(a[1])
    t = 0
    for i in range(1,n+1):
        if a[i] > a[i-1]:
            if a[i] > a[i+1]:
                t += 1
        elif a[i] < a[i-1]:
            if a[i] < a[i+1]:
                t += 1
    print(t)