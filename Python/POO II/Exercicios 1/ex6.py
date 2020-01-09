# -*- coding: utf-8 -*-
n = int(input())
n -= 1
sum = 0
for i in range(n,0,-1):
    if i%3==0:
        sum += i
print(sum)