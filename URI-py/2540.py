# -*- coding: utf-8 -*-
while True:
    try:
        n = int(input())
        v = input().split()
        qtde = 0
        for i in range(0,n):
            if v[i] == "1":
                qtde += 1
        if qtde >= n * 2 / 3:
            print("impeachment")
        else:
            print("acusacao arquivada")
    except EOFError:
        break
