# -*- coding: utf-8 -*-
lista = []
c = 0
qua = int(input())
while c < qua:
    x, y = map(int,input().split())
    if x < y:
        lista.append([x,y])
    elif x > y:
        lista.append([y,x])
    else:
        lista.append([x,y])
    c += 1
for a in lista:
    s = 0
    for i in range(a[0]+1,a[1]):
        if (i%2)!=0:
            s += i
    print(s)
