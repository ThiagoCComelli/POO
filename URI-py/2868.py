# -*- coding: utf-8 -*-
for i in range(int(input())):
    v1,op,v2,nd,res = input().split()
    v1,v2,res = int(v1),int(v2),int(res)
    if op == "+":
        valor = v1 + v2
    elif op == "-":
        valor = v1 - v2
    else:
        valor = v1 * v2

    qr = "r" * abs(valor - res)
    print("E{}sou!".format(qr))