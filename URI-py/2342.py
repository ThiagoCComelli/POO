# -*- coding: utf-8 -*-
n = int(input())
dados = str(input())
dados = dados.split()
if dados[1] == "+":
    s = int(dados[0]) + int(dados[2])
    if s<=n:
        print("OK")
    else:
        print("OVERFLOW")
elif dados[1] == "*":
    s = int(dados[0]) * int(dados[2])
    if s<=n:
        print("OK")
    else:
        print("OVERFLOW")
