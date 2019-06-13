# -*- coding: utf-8 -*-
import re

texto = ""
for i in range(int(input())):
    text = input()

    for u in text:
        if re.match("[a-zA-Z]",u):
            texto += chr(ord(u)+3)
        else:
            texto += u
    texto = texto[::-1]
    meio = int((len(texto)/2))
    met = texto[0:meio]
    met1 = texto[meio:]
    met2 = ""

    for u in met1:
        met2 += chr(ord(u)-1)
    print(met+met2)