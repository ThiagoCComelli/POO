# -*- coding: utf-8 -*-
alcool = 0
gasolina = 0
diesel = 0
n = int(input())
while True:
    if n == 1:
        alcool += 1
    elif n == 2:
        gasolina += 1
    elif n == 3:
        diesel += 1
    elif n == 4:
        break
    n = int(input())
print("MUITO OBRIGADO\nAlcool: %d\nGasolina: %d\nDiesel: %d"%(alcool,gasolina,diesel))
