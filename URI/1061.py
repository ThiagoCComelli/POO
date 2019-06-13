# -*- coding: utf-8 -*-
diainicial = input().split(" ")
di = int(diainicial[1])
horainicial = input().split(" ")
x = int(horainicial[0])
y = int(horainicial[2])
z = int(horainicial[4])

diafinal = input().split(" ")
df = int(diafinal[1])
horafinal = input().split(" ")
x1 = int(horafinal[0])
y1 = int(horafinal[2])
z1 = int(horafinal[4])

dia = df-di
hora = x1-x

if hora < 0:
    hora = 24 + hora
    dia -= 1

minuto = y1-y

if minuto < 0:
    minuto = 60 + minuto
    hora -= 1

segundos = z1-z

if segundos < 0:
    segundos = 60 + segundos
    minuto -= 1

if dia <= 0:
    dia = 0

print("%d dia(s)"%dia)
print("%d hora(s)"%hora)
print("%d minuto(s)"%minuto)
print("%d segundo(s)"%segundos)
