# -*- coding: utf-8 -*-
n,k = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
a = True
t = 0
for i in range(1,n-1):
    if l[i] > l[i+1]:
        if l[i] > l[i-1]:
            t += 1
if t == k:
    print('beautiful')
else:
    print('ugly')

