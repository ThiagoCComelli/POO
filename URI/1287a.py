# -*- coding: utf-8 -*-
def ver(frase):
    nome = ''
    num = '1234567890'

while True:
    try:
        frase = input()
        frase = ver(frase)
        print(frase)
    except EOFError:
        break