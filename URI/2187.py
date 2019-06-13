# -*- coding: utf-8 -*-
teste = 1
while True:
    valor = int(input())
    if valor == 0:
        break
    b = ["0"] * 4
    if valor >= 50:
        b[0] = str(valor//50)
        valor = valor%50
    if valor >= 10:
        b[1] = str(valor//10)
        valor = valor%10
    if valor >= 5:
        b[2] = str(valor//5)
        valor = valor%5
    b[3] = str(valor)
    print("Teste %d"%teste)
    print(" ".join(b))
    print()
    teste += 1

