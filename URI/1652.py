# -*- coding: utf-8 -*-
l,n = map(int,input().split())
lista = [] # corrigir
dic = {}
a = 'aeiou'
for i in range(l):
    s,p = input().split()
    dic[s] = p
for i in range(n):
    lista.append(input())
for i in lista:
    if i in dic:
        print(dic[i])
    else:
        if i[-1:] == 'y':
            if i[-2:-1] in a:
                print(i+'s')
            else:
                print(i[:-1]+'ies')
        elif i[-1:] == 'o' or i[-1:] == 's' or i[-1:] == 'x':
            print(i+'es')
        elif i[-2:] == 'ch' or i[-2:] == 'sh':
            print(i+'es')
        else:
            print(i+'s')