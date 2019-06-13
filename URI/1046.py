# -*- coding: utf-8 -*-
i, f = map(int, input().split())
if i == f:
    print("O JOGO DUROU 24 HORA(S)")
elif f > i:
    h = f - i
    print("O JOGO DUROU %d HORA(S)"%h)
elif i > f:
    h = (24-i)+f
    print("O JOGO DUROU %d HORA(S)"%h)
