# -*- coding: utf-8 -*-
s = 0
q = 0
while True:
    try:
        n = input()
        q += 1
        s += int(input())
    except EOFError:
        break
print("%.1f"%(s/q))
