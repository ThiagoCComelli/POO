# -*- coding: utf-8 -*-
n = int(input())
for _ in range (0,n+1):
    a = int(input())
    if a == 0:
        print("NULL")
    elif a % 2 == 0:
        if _ > 0:
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    elif a % 2 != 0:
        if _ > 0:
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")
