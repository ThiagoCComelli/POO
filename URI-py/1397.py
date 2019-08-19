# -*- coding: utf-8 -*-
while True:
    A = 0
    B = 0
    n = int(input())
    if n==0:
        break
    for i in range (n):
        a, b = map(int, input().split())
        if a>b:
            A += 1
        elif b>a:
            B += 1
        elif a==0 or b==0:
            B+=0
            A+=0
    print(A,B)
