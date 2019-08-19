# -*- coding: utf-8 -*-
while True:

    try:
        n = map(int,input().split())
        print(max(n))
    except EOFError:
        break