# -*- coding: utf-8 -*-
n = int(input())
listap = []
listai = []
lista = []
for i in range(n):
    v = int(input())
    if v%2==0:
        listap.append(v)
    else:
        listai.append(v)
listap.sort()
listai.sort(reverse=True)
for i in listap:
    print(i)
for i in listai:
    print(i)
