# -*- coding: utf-8 -*-
while(True):
    n = int(input())
    if n != 0:
        fat,fatAnterior = 0, 0
        i = 1
        while(True):
            fat = 0
            for x in range(i,0,-1):
                fat += x
            i += 1
            if(fat>n):
                break
            else:
                fatAnterior = fat
        p = n - fatAnterior
        f = fatAnterior
        print("%d %d"%(f,p))
    else:
        break
