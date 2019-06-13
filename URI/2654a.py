# -*- coding: utf-8 -*-
n = int(input())
dic = {}
#maior = 0
for i in range(n):
    d = input().split()
    dic[d[0]] = int(d[1])
#    if int(d[1]) > int(maior):
#        maior = d[1]
dic = dict(map(reversed, dic.items()))
print(dic)
print(dic[max(dic)])