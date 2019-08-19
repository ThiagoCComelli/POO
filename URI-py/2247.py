# -*- coding: utf-8 -*-
teste = 1
while True:
    x = int(input())
    if x == 0:
        break
    s = 0
    print("Teste %d"%teste)
    teste += 1
    for i in range(x):
        x, y = map(int,input().split())
        s += x - y
        print(s)

