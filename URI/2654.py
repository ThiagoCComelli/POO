# -*- coding: utf-8 -*-
n = int(input())
poder = {}
deus = {}
morte = {}
for i in range(n):
    d = input().split()
    poder[d[0]] = int(d[1])
    deus[d[0]] = int(d[2])
    morte[d[0]] = int(d[3])
poder = dict(map(reversed, poder.items()))
deus = dict(map(reversed, deus.items()))
morte = dict(map(reversed, morte.items()))
print(poder[max(poder)])
print(poder)
print(deus)
print(morte)