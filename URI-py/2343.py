# -*- coding: utf-8 -*-
n = int(input())
v = input().split()
v = str(v)
if v[1] == "+":
    if n == (int(v[0])+int(v[2])):
        print("OK")
