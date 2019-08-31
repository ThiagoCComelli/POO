# -*- coding: utf-8 -*-
n = int(input())
tot = 0
for i in range(n):
    m = input()
    stri = []

    for u in m:
        if u != ".":
            stri.append(u)
    print(stri)
    while True:
        for j in range(0,len(stri)-1):
            if stri[j] == "<":
                if stri[j+1] == ">":
                    print('s')
        break
    print(tot)
