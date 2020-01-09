# -*- coding: utf-8 -*-
n,m = map(int,input().split())
sum = 0
for i in range(m):
    if i == 0:
        sum += n
    else:
        sum *= n
print(sum)

sum = 0
qtde = 0
while qtde < m:
    if qtde == 0:
        sum += n
    else:
        sum *= n
    qtde += 1
print(sum)
print(pow(n,m))
