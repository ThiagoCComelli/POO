# -*- coding: utf-8 -*-
while True:
    try:
        n = input()
        lista = []
        lista1 = []
        c = False
        d = False
        cpf = False
        for i in n:
            if i.isdigit() == True:
                lista.append(int(i))

        for i in range(len(lista) - 2):
            lista1.append(lista[i])

        tot = 0
        for i in range(len(lista1)):
            b = (i+1) * lista1[i]
            tot += b
        a = tot%11
        if a == 10:
            a = 0

        if a == lista[-2]:
            d = True

        lista1 = lista1[::-1]
        tot = 0
        for i in range(len(lista1)):
            b = (i+1) * lista1[i]
            tot += b
        a = tot % 11
        if a == 10:
            a = 0
        if a == lista[-1]:
            c = True

        if c == True and d == True:
            print('CPF valido')
        else:
            print('CPF invalido')

    except EOFError:
        break