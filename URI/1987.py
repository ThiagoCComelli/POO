# -*- coding: utf-8 -*-
while True:
    try:
        s = 0
        n = input()
        n = str(n).split()
        for i in n[1]:
            s += int(i)
        if s%3==0:
            print("%d sim"%s)
        else:
            print("%d nao"%s)
    except EOFError:
        break
