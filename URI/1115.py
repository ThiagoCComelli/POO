# -*- coding: utf-8 -*-
while True:
    x, y = map(int,input().split())
    if (x==0) or (y==0):
        break
    elif x>0:
        if y>0:
            print("primeiro")
        elif y<0:
            print("quarto")
    elif x<0:
        if y<0:
            print("terceiro")
        elif y>0:
            print("segundo")
