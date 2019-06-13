# -*- coding: utf-8 -*-
while True:
    n = input()
    if n == "*":
        break
    n = n.split()
    s = 0
    for i in range(len(n)-1):
        if n[i][:1].upper() == n[i+1][:1].upper():
            s = 1
        else:
            s = 0
    if s == 0:
        print("N")
    else:
        print("Y")
