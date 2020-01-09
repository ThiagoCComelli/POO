# -*- coding: utf-8 -*-
n,m= map(int,input().split())
sum = 0
if n > m:
    for i in range(m,n+1):
        if i%2!=0:
            print(i)
            sum += i
    qtde = n-m
elif m > n:
    for i in range(n,m+1):
        if i % 2 != 0:
            print(i)
            sum += i
    qtde = m-n
else:
    sum += m + n
print(sum)
print(int(sum/qtde))
