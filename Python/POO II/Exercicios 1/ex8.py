# -*- coding: utf-8 -*-
n = int(input())
outro = 0
for i in range(1,n+1):
    if i%3==0:
        outro += i
    if i%5==0:
        outro += i
    if i%7==0:
        outro += i
    if i%8==0:
        outro -= i
print(outro)
