# -*- coding: utf-8 -*-

while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    lista = []
    for i in range(n):
        lista.append(input())
    print(*lista,sep="\n")
    print()