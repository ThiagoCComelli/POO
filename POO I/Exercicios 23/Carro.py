# -*- coding: utf-8 -*-
from datetime import datetime
class Carro():
    def __init__(self,rodas = None,volante = None,motor = None,tanque = None,velocidade = None,marca = None):
        self.__rodas = rodas
        self.__volante = volante
        self.__motor = motor
        self.__tanque = tanque
        self.__velocidade = velocidade
        self.__marca = marca

    def carroCompleto(self):
        if len(self.__rodas) == 4 and self.__volante != None and self.__motor != None and self.__tanque != None:
            return 'Completo'
        else:
            return 'Incompleto'

    def situacaoTanque(self):
        if self.__tanque.getCombus() <= self.__tanque.getCapacidade() * 0.10:
            return 0
        elif self.__tanque.getCombus() <= self.__tanque.getCapacidade() * 0.25:
            return 1
        elif self.__tanque.getCombus() <= self.__tanque.getCapacidade() * 0.35:
            return 2
        else:
            return 3

    def abastecer(self,x):
        if (self.__tanque.getCombus() + x) > self.__tanque.getCapacidade():
            self.__tanque.setCombus0()
        else:
            self.__tanque.setCombus(x)

        print('Capacidade: {}, Combustivel: {}, Apos o abstecimento[situacao]: {}'.format(self.__tanque.getCapacidade(),self.__tanque.getCombus(),self.situacaoTanque()))

    def getTanque(self):
        return self.__tanque

    def __repr__(self):
        return 'Marca: {}, Velocidade {}, Volante: {}, Motor: {} {}, Capacidade: {}, Combustivel: {}, Completo: {}, Situação do tanque: {}'\
            .format(self.__marca,self.__velocidade,self.__volante.getMarca(),self.__motor.getMarca(),self.__motor.getPotencia(),self.__tanque.getCapacidade(),self.__tanque.getCombus(),self.carroCompleto(),self.situacaoTanque())

class Roda():
    def __init__(self,marca,troca = datetime.now()):
        self.__marca = marca
        self.__troca = troca

    def getMarca(self):
        return self.__marca
    def getTroca(self):
        return self.__troca

    def setTroca(self):
        self.__troca = troca

class Volante():
    def __init__(self,marca):
        self.__marca = marca

    def getMarca(self):
        return self.__marca
    def setMarca(self,marca):
        self.__marca = marca

class Motor():
    def __init__(self,marca,potencia):
        self.__marca = marca
        self.__potencia = potencia

    def getMarca(self):
        return self.__marca
    def getPotencia(self):
        return self.__potencia

    def setMarca(self,marca):
        self.__marca = marca
    def setPotencia(self,potencia):
        self.__potencia = potencia

class Tanque():
    def __init__(self,capacidade,combus):
        self.__capacidade = capacidade
        self.__combus = combus

    def getCapacidade(self):
        return self.__capacidade
    def getCombus(self):
        return self.__combus

    def setCombus0(self):
        self.__combus = self.__capacidade
    def setCombus(self,x):
        self.__combus += x

rodas = []
rodas.append(Roda('Michelin'))
rodas.append(Roda('Michelin'))
rodas.append(Roda('Custons'))
rodas.append(Roda('Petrobras'))

rodas2 = []
rodas2.append(Roda('abc'))
rodas2.append(Roda('dsf'))
rodas2.append(Roda('asd'))
rodas2.append(Roda('qwe'))

carro1 = Carro(rodas,Volante('Fiat'),Motor('Ford',620),Tanque(150,100),180,'Ford')
carro2 = Carro(rodas[0:2],Volante('Ford'),Motor('Ford',600),Tanque(100,35),180,'Ford')
carro3 = Carro(rodas2,Volante('Renault'),Motor('Ford',620),Tanque(150,12),180,'Renault')
carro4 = Carro(rodas2,Volante('Mustang'),Motor('Ford',620),Tanque(150,20),180,'Mustang')

print(carro1)
print(carro2)
print(carro3)
print(carro4)

carro1.abastecer(50)
carro2.abastecer(50)
carro3.abastecer(50)
carro4.abastecer(50)

print(carro1)
print(carro2)
print(carro3)
print(carro4)



