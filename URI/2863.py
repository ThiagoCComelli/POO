# -*- coding: utf-8 -*-
while True:
    try:
        maior = 100
        for i in range(int(input())):
            n = float(input())
            if n < maior:
                maior = n
        print(maior)
    except EOFError:
        break