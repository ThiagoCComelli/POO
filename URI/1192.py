# -*- coding: utf-8 -*-
n = int(input())
for i in range(n):
    v = input()
    if v[1] == v[1].upper():
        if v[0] == v[2]:
            print(int(v[0])*int(v[2]))
        else:
            print(int(v[2])-int(v[0]))
    elif v[1] == v[1].lower():
        if v[0] == v[2]:
            print(int(v[0]) * int(v[2]))
        else:
            print(int(v[2]) + int(v[0]))
