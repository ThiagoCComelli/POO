# -*- coding: utf-8 -*-
while True:
    try:
        casos = 1
        soma = 0
        n = int(input())
        for i in range(n):

        print("Caso %d: %d numero"%(casos,soma))
        casos += 1
    except EOFError:
        break
