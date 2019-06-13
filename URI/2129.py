# -*- coding: utf-8 -*-
instancia = 1
while True:
    try:
        n = int(input())
        s = 1
        i = 2
        lista = []
        lista1 = []
        while i <= n:
            s *= i
            i += 1
        print("Instancia %d"%instancia)
        instancia += 1
        lista.append(str(s))
        for i in lista:
            for u in i:
                if u != "0":
                    lista1.append(u)
        print(lista1[-1])
        print()
    except EOFError:
        break
