# -*- coding: utf-8 -*-
class Conta():
    def __init__(self,numero,agencia,cliente,gerente):
        self.__numero = numero
        self.__agencia = agencia
        self.__cliente = cliente
        self.__gerente = gerente
        self.__saldo = 0
        self.__cliente.addconta(self)
        self.__gerente.addconta(self)

    def sacar(self,x):
        if self.__saldo - x >= 0:
            self.__saldo -= x
        else:
            return 'saldo insuficiente'
    def depositar(self,x):
        if x > 0:
            self.__saldo += x
        return 'valor invalido'
    def saldo(self):
        return self.__saldo


class Pessoa():
    def __init__(self,nome,anonasci):
        self.__nome = nome
        self.__anonasci = anonasci
        self.__conta = []

    def nome(self):
        return self.__nome
    def contas(self):
        return self.__conta
    def addconta(self,x):
        self.__conta.append(x)
    def qtdecontas(self):
        return len(self.__conta)

class Cliente(Pessoa):
    def __init__(self,nome,anonasci,estado):
        super().__init__(nome,anonasci)
        self.__estado = estado

    def dinheiroTotal(self):
        tot = 0
        for i in self.contas():
            tot += i.saldo()
        return tot

class Gerente(Pessoa):
    def __init__(self,nome,registro,anonasci):
        super().__init__(nome,anonasci)
        self.__registro = registro
    def gerenteadm(self):
        tot = 0
        for i in self.contas():
            tot += i.saldo
        return tot

c0 = Cliente('Thiago C.','28/04/2000','SC')
c1 = Cliente('Thiago Comelli.','28/04/2000','SC')
g0 = Gerente('BomDia','19','01/01/1909')
conta0 = Conta('QWE','QWER',c0,g0)
conta1 = Conta('ASD','ASDF',c1,g0)
conta2 = Conta('QZX','ZXCV',c1,g0)

print('Thiago C. possui %s contas '%c0.qtdecontas())
print('Thiago Comelli. possui %s contas '%c1.qtdecontas())
conta0.depositar(100)
conta1.depositar(10000)
conta2.depositar(1000)
conta1.sacar(11000)
conta1.sacar(1000)
print(conta0.saldo())
print(conta1.saldo())
print(conta2.saldo())
print(c1.dinheiroTotal())
