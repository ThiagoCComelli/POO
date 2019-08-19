# -*- coding: utf-8 -*-
while True:
    try:
        a,b,c = map(int,input().split())
        if a==b==c:
            print("*")
        else:
            if a==b:
                print("C")
            elif a==c:
                print("B")
            elif b==c:
                print("A")
    except (EOFError):
        break

