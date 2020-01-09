# -*- coding: utf-8 -*-
a = float(input())
b = float(input())
temp = 20
while True:
    if b > a:
        print("Temp: {} C".format(temp))
        break
    a += 2
    b += 3.5
    temp += 1
