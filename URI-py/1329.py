# -*- coding: utf-8 -*-
while True:
    v = int(input())
    if v==0:
        break
    else:
        n = list(map(int,input().split()))
        maria0 = 0
        joao1 = 0
        for i in n:
            if i == 0:
                maria0 += 1
            elif i == 1:
                joao1 += 1
        print("Mary won %d times and John won %d times"%(maria0,joao1))
