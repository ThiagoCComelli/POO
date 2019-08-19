# -*- coding: utf-8 -*-
while True:
    lista = [['.', '*', '*', '*', '.', '.'], ['*', '.', '.', '.', '.', '.'], ['*', '.', '*', '.', '.', '.'],
             ['*', '*', '.', '.', '.', '.'],
             ['*', '*', '.', '*', '.', '.'], ['*', '.', '.', '*', '.', '.'], ['*', '*', '*', '.', '.', '.'],
             ['*', '*', '*', '*', '.', '.'], ['*', '.', '*', '*', '.', '.'], ['.', '*', '*', '.', '.', '.'],
             ]
    c = int(input())
    if c == 0:
        break
    else:
        n = input()
        if n == "S":
            n1 = input()
            frase = ""
            frase1 = ""
            frase2 = ""
            for i in n1:
                frase += (lista[int(i)][0]+lista[int(i)][1])
                frase += " "
                frase1 += (lista[int(i)][2] + lista[int(i)][3])
                frase1 += " "
                frase2 += (lista[int(i)][4] + lista[int(i)][5])
                frase2 += " "
            print(frase)
            print(frase1)
            print(frase2)
        elif n == "B":
            lista0 = [".***..","*.....","*.*...","**....","**.*...","*..*..","***...","****..","*.**..",".**..."]
            lista = []
            lista1 = []
            lista2 = []
            lista3 = []
            for i in range(3):
                lista.append(input().split())
            t = 0
            while t < 3:
                for i in range(len(lista)):
                    lista1.append(lista[i][t])
                t += 1
            um = 0
            dois = 3
            for i in range(c):
                lista2.append(lista1[um:dois])
                um += 3
                dois += 3
            for i in lista2:
                frase3 = ""
                for u in i:
                    frase3 += u
                lista3.append(frase3)
            frase2 = ""
            for i in lista3:
                if i in lista0:
                    frase2 += str(lista0.index(i))
            print(frase2)




