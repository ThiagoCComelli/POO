# -*- coding: utf-8 -*-
while True:
    dic = {}
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(n):
            v = input().split()
            dic[v[0]] = v[1]
        n1 = int(input())
        a,total = 0,0
        for i in range(n1):
            c = 0
            v1 = input().split()
            for o in dic[v1[0]]:
                if o != v1[1][c]:
                    a += 1
                c += 1
            if a > 1:
                total += 1
            a = 0
        print(total)


