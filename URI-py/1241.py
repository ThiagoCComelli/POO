# -*- coding: utf-8 -*-
for i in range(int(input())):
    l = input().split()


    if len(l[1]) > len(l[0]):
        print('nao encaixa')
    elif len(l[0]) == len(l[1]) and l[0] == l[1]:
        print('encaixa')
    elif l[0][-len(l[1]):] == l[1]:
        print('encaixa')
    else:
        print('nao encaixa')

