# -*- coding: utf-8 -*-
for i in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    l1 = sorted(l,reverse=True)
    tot = 0
    for i in range(len(l)):
        if l[i] == l1[i]:
            tot += 1
    print(tot)