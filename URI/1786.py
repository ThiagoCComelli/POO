# -*- coding: utf-8 -*-
while True:
    try:
        lista = input()
        lista1 = []
        stra = ''
        s = 0
        for i in lista:
            s += 1
            stra += str(i)
            if s == 3 or s == 6:
                stra += '.'
            if s == 9:
                stra += '-'

        tot = 0
        for i in range(1,len(lista)+1):
            tot += int(i * int(lista[i-1]))
        a = tot%11
        if a == 10:
            a = 0
        stra += str(a)

        tot = 0
        lista = lista[::-1]
        for i in range(1,len(lista)+1):
            tot += int(i * int(lista[i-1]))
        a = tot % 11
        if a == 10:
            a = 0
        stra += str(a)

        print(stra)
    except EOFError:
        break