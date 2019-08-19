# -*- coding: utf-8 -*-
n = int(input())
for _ in range(0,n):
    preco = {}
    total = 0

    n = int(input())
    for _ in range(0,n):
        f,v = input().split()
        v = float(v)
        preco[f] = v

    p = int(input())
    for _ in range(0,p):
        f,q = input().split()
        q = int(q)
        total += preco[f]*q
    print("R$ %.2f"%total)
