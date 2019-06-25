# -*- coding: utf-8 -*-
class Imobiliaria():
    def __init__(self,nome):
        self.__nome = nome
        self.__imoveis = []

class Imovel():
    def __init__(self,modo='aluga',id=0):
        self.__modo = modo
        self.__quartos = []
        self.__banheiros = []
        self.__id = id
        self.__metragem = 0



    def addComodo(self,x):
        if x == 'quarto':
            self.__quartos.append(x)
            self.__metragem += x.getMetragemc()

        elif x == 'banheiro':
            self.__banheiros.append(x)
            self.__metragem += x.getMetragemc()-




    def getMetragem(self):
        return self.__metragem
    def getQuartos(self):
        return self.__quartos
    def getBanheiros(self):
        return self.__banheiros

class Comodo():
    def __init__(self,nome='',metragem=0):
        self.__nome = nome
        self.__metragemc = metragem

    def getMetragemc(self):
        return self.__metragemc
    def getNome(self):
        return self.__nome



com0 = Comodo('quarto',100)
imo0 = Imovel()
imo0.addComodo(com0)
print(imo0.getMetragem())
print(com0.getMetragemc())