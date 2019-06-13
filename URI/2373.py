# -*- coding: utf-8 -*-
n = int(input())
quebrou = 0
while n > 0:
    n -= 1
    l, c = map(int,input().split())
    if l > c:
        quebrou += c
print(quebrou)
