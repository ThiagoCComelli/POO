# -*- coding: utf-8 -*-
n = str(input())
frase = input().split()
s = 0
for i in frase:
    for u in set(i):
        if u == n:
            s += 1
print("%.1f"%((s/int(len(frase)))*100))
