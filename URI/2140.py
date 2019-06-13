# -*- coding: utf-8 -*-
while True:
    x,y = map(int,input().split())
    r = abs(x-y)
    if (r==7 or r==12 or r==22 or r==52 or r==102 or r==15 or r==25 or r==55 or r==105 or r==30 or r==60 or r==110 or r==70 or r==120 or r==150):
        print("possible")
    elif x==0 and y==0:
        break
    else:
        print("impossible")

