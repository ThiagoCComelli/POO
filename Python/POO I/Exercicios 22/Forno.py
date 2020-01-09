# -*- coding: utf-8 -*-
class Forno:
    __temp = 50
    __status = 0
    def __init__(self,marca, tempm):
        self.__marca = marca
        self.__tempm = tempm

    def setLigar(self):
        self.__status = 1
    def setDesligado(self):
        self.__status = 0
    def setAumentar(self,aumentar):
        if self.__temp == self.__tempm:
            return False
        elif (self.__temp + aumentar) > self.__tempm:
            return False
        else:
            self.__temp += aumentar
    def setDiminuir(self,diminuir):
        if self.__temp == 50:
            return False
        elif (self.__temp - diminuir) < 50:
            return False
        else:
            self.__temp -= diminuir

    def getTemp(self):
        return self.__temp
    def getStatus(self):
        return self.__status
    def getMarca(self):
        return self.__marca

#A
t = Forno('Tabajra',100)
#B
o = Forno('Orange',350)
#C
t.setLigar()
#D
print(t.getTemp())
#E
t.setAumentar(25)
#F
print(t.getTemp())
#G
t.setAumentar(30)
#H
print(t.getTemp())
#I
t.setDiminuir(15)
#J
print(t.getTemp())
#K
t.setDiminuir(75)

print()

#L
o.setLigar()
#M
print(o.getTemp())
#N
o.setAumentar(300)
#O
print(o.getTemp())
#P
o.setDiminuir(20)
#Q
print(o.getTemp())
#R
o.setAumentar(30)
#S
print(o.getTemp())

print()

#T
print(o.getStatus())
#U
print(t.getStatus())

#V
o.setDesligado()
t.setDesligado()
#W
print(o.getStatus())
#X
print(t.getStatus())

print()

#Y
print(t.getMarca())
print(o.getMarca())

