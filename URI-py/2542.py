# -*- coding: utf-8 -*-
while True:
    try:
        marcos = []
        leonardo = []
        atributos = int(input())
        qtde = [int(x) for x in input().split()]
        for i in range(qtde[0]):
            marcos.append([int(x) for x in input().split()])
        for i in range(qtde[1]):
            leonardo.append([int(x) for x in input().split()])
        carta = [int(x) for x in input().split()]
        poder = int(input())
        if marcos[carta[0]-1][poder-1] == leonardo[carta[1]-1][poder-1]:
            print("Empate")
        elif marcos[carta[0]-1][poder-1] < leonardo[carta[1]-1][poder-1]:
            print("Leonardo")
        else:
            print("Marcos")
    except EOFError:
        break