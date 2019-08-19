# -*- coding: utf-8 -*-
resposta = {"esquerda" : "ingles",
            "direita" : "frances",
            "nenhuma" : "portugues",
            "as duas" : "caiu"}
while True:
    try:
        s = input()
        print(resposta[s])
    except EOFError:
        break