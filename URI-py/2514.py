# -*- coding: utf-8 -*-
while True:
    try:
        def maximo(x,y,z):
            if x >= y:
                largest = x
            elif y >= x:
                largest = y
            else:
                largest = z
            while True:
                if largest % x == 0 and largest % y == 0 and largest % z == 0:
                    return largest
                else:
                    largest += 1
        n = int(input())
        n1 = [int(x) for x in input().split()]
        print(maximo(n1[0],n1[1],n1[2])-n)
    except EOFError:
        break