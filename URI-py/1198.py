# -*- coding: utf-8 -*-
while True:
    try:
        v1,v2 = map(int,input().split())
        print(abs(v1-v2))
    except EOFError:
        break
