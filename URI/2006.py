# -*- coding: utf-8 -*-
cha = int(input())
a, b, c, d, e = map(int,input().split())
s = 0
if a==cha:
    s+=1
if b==cha:
    s+=1
if c==cha:
    s+=1
if d==cha:
    s+=1
if e==cha:
    s+=1
print(s)
