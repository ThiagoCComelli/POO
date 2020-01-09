# -*- coding: utf-8 -*-
class Leilao():
    __maiorValor = 0
    __nomeMaiorvalor = 'Ninguem'
    __qtde = 0
    __tot = 0
    __estado = 0
    __valores = []
    def __init__(self,obj,minimo):
        self.__obj = obj
        self.__minimo = minimo

    def lance(self,nome,lance):
        if self.__estado == 1 and lance >= self.__minimo:
            if lance > self.__maiorValor:
                self.__maiorValor = lance
                self.__nomeMaiorvalor = nome
            self.__qtde += 1
            self.__tot += lance
            self.__valores.append(lance)
        else:
            return False

    def Iniciar(self):
        self.__estado = 1
    def Encerrar(self):
        self.__estado = 2

    def porcentual(self):
        if (self.__maiorValor/self.__minimo)-1 >= 0:
            return ((self.__maiorValor/self.__minimo)-1) * 100

    def __repr__(self):
        if self.__estado == 0:
            return 'nao iniciado'
        elif self.__estado == 1:
            return 'em andamento'
        else:
            return 'Objeto: {}\nLance: {} R$\nVencedor: {}\nMinimo: {} R$\nQtde lances: {}\nValore medio: {:.1f} R$\nLucro acima: {:.1f}%%'\
                .format(self.__obj,self.__maiorValor,self.__nomeMaiorvalor,self.__minimo,self.__qtde,self.__tot/(len(self.__valores)),Leilao.porcentual(self))

a = Leilao('Carro',130)
a.Iniciar()
a.lance('clara',120)
a.lance('viot',200)
a.lance('viotasd',230)
a.lance('viot',250)
a.Encerrar()
print(a)

print()
b = Leilao('Moto',100)
print(b)



