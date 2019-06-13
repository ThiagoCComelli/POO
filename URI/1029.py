# -*- coding: utf-8 -*-
n = int(input())
for i in range(n):
    t = 0
    t1 = 0
    def fatorial(x):
        global t; global t1
        if x == 0:
            t += 1
            return 1
        t += 2
        return x * fatorial(x-1)
    a = int(input())
    print(fatorial(a))
    print(t)