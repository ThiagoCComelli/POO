# -*- coding: utf-8 -*-
while True:
    try:
        f, v = map(int,input().split())
        voltaram = input().split()
        total = []
        for a in range(v):
            voltaram[a] = int(voltaram[a])
        if f == v:
            print("*")
        elif f!=v:
            for i in range(f):
                total.append(i+1)
            for u in voltaram:
                total.remove(u)
            print(*total, end=" \n")
    except EOFError:
        break
