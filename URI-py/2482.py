# -*- coding: utf-8 -*-
n = int(input())
dic = {}
for i in range(n):
    s = input()
    l = input()
    dic[s] = l
n1 = int(input())
for i in range(n1):
    nome = input()
    lingua = input()
    print("%s\n%s\n"%(nome,dic[lingua]))