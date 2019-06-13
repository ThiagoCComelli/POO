# -*- coding: utf-8 -*-
x1, y1, x2, y2 = map(int,input().split())
while True:
    if (x1 and x2 and y1 and y2)==0:
        break
    elif x1 == x2 and y1 == y2:
        print("0")
        x1, y1, x2, y2 = map(int, input().split())
    elif (x1==x2) and (y1 != y2):
        print("1")
        x1, y1, x2, y2 = map(int, input().split())
    elif (y1==y2) and (x1 != x2):
        print("1")
        x1, y1, x2, y2 = map(int, input().split())
    elif (abs(x1-x2)==abs(y1-y2)):
        print("1")
        x1, y1, x2, y2 = map(int, input().split())
    else:
        print("2")
        x1, y1, x2, y2 = map(int, input().split())
