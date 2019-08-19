# -*- coding: utf-8 -*-
def primo():
    m = int(input())
    c = True
    c1 = False
    if m == 1:
        return c1
    i = 2
    while i**2 <= m:
        if m%i==0:
            return c1
        i+=1
    return c
n = int(input())
for i in range(n):
    if primo()==True:
        print("Prime")
    else:
        print("Not Prime")