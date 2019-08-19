# -*- coding: utf-8 -*-
while True:
    try:
        n = input()
        lista = []
        pala = ''
        for i in range(len(n)):
            if i < len(n)-1:
                pala += n[i] + ' '
            else:
                pala += n[i]
        s = 0
        for i in range(len(n)):
            if i != 0:
                print(i*" "+pala[:-s])
                s += 2
            else:
                print(pala)
                s += 2
        print()
    except EOFError:
        break