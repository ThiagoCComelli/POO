# -*- coding: utf-8 -*-
for i in range(int(input())):
    frase = input().split()
    nfrase = ""
    a = frase[0]
    b = frase[1]
    if len(frase[0]) >= len(a):
        for i in range(len(a)):
            nfrase += a[i]+b[i]
        nfrase += a[len(b):]
        print(nfrase)
    elif len(b) > len(a):
        for j in range(len(b)):
            nfrase += a[i] + b[i]
        nfrase += b[len(a):]
        print(nfrase)