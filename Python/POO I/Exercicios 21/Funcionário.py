# -*- coding: utf-8 -*-
class Funcionario:
    __cargo,__vendas,__salario = '',0,0
    def __init__(self,nome = '',idade = 0,salariob = 0):
        self.__nome = nome
        self.__idade = idade
        self.__salariob = salariob
    def getNome(self):
        return self.__nome
    def getIdade(self):
        return self.__idade
    def getSalariob(self):
        return self.__salariob
    def getCargo(self):
        return self.__cargo
    def getVendas(self):
        return self.__vendas

    def setNome(self,nome):
        self.__nome = nome
    def setIdade(self,idade):
        self.__idade = idade
    def setSalariob(self,salariob):
        self.__salariob = salariob
    def setCargo(self,cargo):
        self.__cargo = cargo
    def setVendas(self,vendas):
        self.__vendas = vendas

    def darAumento(self,a):
        self.__salariob = ((a/100)*self.__salariob)+self.__salariob
    def calcSalario(self):
        total = (self.__salariob)+(self.__vendas)*0.04
        return total
    def calImposto(self):
        total = (self.__salariob)+(self.__vendas)*0.04
        if total <= 1000:
            total = total*0.05
        elif 1000 < total <= 5000:
            total = total*0.08
        elif 5000 < total <= 10000:
            total = total*0.12
        else:
            total = total-total*0.20
        return total
    def calComissao(self):
        total = self.__vendas * 0.04
        return total


#ABC
bob = Funcionario('Bob',23,3900)
tom = Funcionario('Tom',27,1200)
tonin = Funcionario('Tonin',27,10000)
#DE
bob.setCargo('Vendedor')
tom.setCargo('Vendedor')
tonin.setCargo('Gerente')
#FGH
bob.setVendas(1000)
tom.setVendas(5000)
tonin.setVendas(1500)
#IJ
bob.darAumento(10)
tom.darAumento(5)
#K
print(bob.getNome())
print(bob.getIdade())
print(bob.getCargo())
print(bob.getVendas())
print(bob.getSalariob())
print(bob.calComissao())
print(bob.calImposto())
print(bob.calcSalario())
print()
print(tom.getNome())
print(tom.getIdade())
print(tom.getCargo())
print(tom.getVendas())
print(tom.getSalariob())
print(tom.calComissao())
print(tom.calImposto())
print(tom.calcSalario())
print()
print(tonin.getNome())
print(tonin.getIdade())
print(tonin.getCargo())
print(tonin.getVendas())
print(tonin.getSalariob())
print(tonin.calComissao())
print(tonin.calImposto())
print(tonin.calcSalario())