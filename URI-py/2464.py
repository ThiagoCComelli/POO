# -*- coding: utf-8 -*-
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
alfabeto1 = input()
decifrar = input()
frase = ''
for i in decifrar:
    a = alfabeto.index(i)
    frase += alfabeto1[a]
print(frase)
