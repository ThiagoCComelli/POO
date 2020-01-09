# -*- coding: utf-8 -*-
n = int(input())
n -= 1
while True:
    if n%2==0:
        print(n)
        n -= 2
    else:
        n -= 1
    if n==0:
        break
