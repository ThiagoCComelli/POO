# -*- coding: utf-8 -*-
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    frase = [int(x) for x in input().split()]
    t = 0
    for i in set(frase):
        if frase.count(i) > 1:
            t += 1
    print(t)
