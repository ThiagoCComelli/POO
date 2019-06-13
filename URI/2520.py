# -*- coding: utf-8 -*-
while True:
    try:
        n,m = [int(x) for x in input().split()]
        lista = []
        a = 0
        b = 0
        for i in range(n):
            lista.append([int(x) for x in input().split()])
        for i in lista:
            print(i)
            if i.count(0) != m:
                if i.count(1) == 1:
                    a += i.index(max(i))+1
                    print(i.index(max(i))+1)
                    a += lista.index(i)+1
                    print(lista.index(i)+1)
                if i.count(2) == 1:
                    b += i.index(max(i))+1
                    print(i.index(max(i))+1)
                    b += lista.index(i)+1
                    print(lista.index(i)+1)
        print(abs(a-b))

    except EOFError:
        break
