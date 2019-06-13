# -*- coding: utf-8 -*-
l,c,m,n = map(int,input().split())
lista = []
lista1 = []
for i in range(l):
    lista.append([int(x) for x in input().split()])
lmax = 0 + m
cmax = 0 + n
lmin = 0
cmin = 0
while True:
    t = 0
    for i in range(lmin,lmax):
        for j in range(cmin,cmax):
            t += lista[i][j]
    cmax += n
    cmin += n
    lista1.append(t)
    if cmax > c:
        cmax = 0+n
        cmin = 0
        lmax += m
        lmin += m
        if lmax > l:
            break
print(max(lista1))





