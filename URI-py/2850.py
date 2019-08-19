# -*- coding: utf-8 -*-
while True:
    try:
        s = input()
        if s == "nenhuma":
            print("portugues")
        elif s == "esquerda":
            print("ingles")
        elif s == "direita":
            print("frances")
        elif s == "as duas":
            print("caiu")
    except EOFError:
        break
