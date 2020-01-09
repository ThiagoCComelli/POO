# -*- coding: utf-8 -*-
class Viagem:
    def __init__(self,destino = '',datein = '',dateout = '',qtde = 0,febre = False,hotel = 0,passagem = 0,seguro = 0):
        self.__destino = destino
        self.__datein = datein
        self.__dateout = dateout
        self.__qtde = qtde
        self.__febre = febre
        self.__hotel = hotel
        self.__passagem = passagem
        self.__seguro = seguro
    def getDestino(self):
        return self.__destino
    def getQtde(self):
        return self.__qtde
    def getFebre(self):
        return self.__febre
    def getHotel(self):
        return self.__hotel
    def getPassagem(self):
        return self.__passagem
    def getSeguro(self):
        return self.__seguro
    def getDatein(self):
        return self.__datein
    def getDateout(self):
        return self.__dateout
    def setDestino(self,destino):
        self.__destino = destino
    def setQtde(self,qtde):
        self.__qtde = qtde
    def setFebre(self,febre):
        self.__febre = febre
    def setHotel(self,hotel):
        self.__hotel = hotel
    def setPassagem(self,passagem):
        self.__passagem = passagem
    def setSeguro(self,seguro):
        self.__seguro = seguro
    def setDatein(self,datein):
        self.__datein = datein
    def setDateout(self,dateout):
        self.__dateout = dateout
    def calculaCustoTotal(self):
        return (self.__passagem + self.__hotel + self.__seguro)

#A
v = Viagem('Roma','10/03/2019','12/05/2019')
#B
v.setQtde(3)
#C
v.setFebre(False)
#D
v.setHotel(1000)
v.setPassagem(2000)
v.setSeguro(120)
#E
v2 = Viagem('Istanbul','14/06/2019','12/07/2019')
#F
v2.setQtde(2)
#G
v2.setFebre(True)
#H
v2.setHotel(2500)
v2.setPassagem(1200)
v2.setSeguro(150)
#I
print(v.getDestino())
print(v.getDatein())
print(v.getDateout())
print(v.getFebre())
print(v.getPassagem())
print(v.getHotel())
print(v.getSeguro())
print(v.getQtde())
print(v.calculaCustoTotal()*v.getQtde())
print()
print(v2.getDestino())
print(v2.getDatein())
print(v2.getDateout())
print(v2.getFebre())
print(v2.getPassagem())
print(v2.getHotel())
print(v2.getSeguro())
print(v2.getQtde())
print(v2.calculaCustoTotal()*v2.getQtde())
print()
#J
if v.calculaCustoTotal()*v.getQtde() < v2.calculaCustoTotal()*v2.getQtde():
    print(v.getDestino())
else:
    print(v2.getDestino())
#K
if v.calculaCustoTotal() < v2.calculaCustoTotal():
    print(v.getDestino())
else:
    print(v2.getDestino())
print()
#L
v.setQtde(2)
#M
if v.calculaCustoTotal()*v.getQtde() < v2.calculaCustoTotal()*v2.getQtde():
    print(v.getDestino())
else:
    print(v2.getDestino())
#N
if v.calculaCustoTotal() < v2.calculaCustoTotal():
    print(v.getDestino())
else:
    print(v2.getDestino())
