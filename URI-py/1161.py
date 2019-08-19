# -*- coding: utf-8 -*-
while True:
    try:
        def fatorial(x):
            if x == 0:
                return 1
            return x * fatorial (x-1)
        a,b = map(int,input().split())
        print(fatorial(a)+fatorial(b))
    except EOFError:
        break