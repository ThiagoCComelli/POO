# -*- coding: utf-8 -*-




class Conta():
    def __init__(self,numero='xxxx',agencia='xxx'):
        self.__numero = numero
        self.__agencia = agencia
        self.__saldo = 0
        self.__gerente = ''
        self.__cliente = ''

    def getNumero(self):
        return self.__numero
    def getAgencia(self):
        return self.__agencia
    def getSaldo(self):
        return self.__saldo
    def getGerente(self):
        return self.__gerente
    def getCliente(self):
        return self.__cliente

    def deposito(self,x):
        if x >= 0:
            self.__saldo += x

    def saque(self,x):
        if x >= 0:
            if x <= self.getSaldo():
                self.__saldo -= x
    def setGerente(self,x):
        self.__gerente = x.getNome()
    def setCliente(self,x):
        self.__cliente = x.getNome()


    def __repr__(self):
        return 'Cliente: {}\nGerente: {}\nSaldo: {}\nAgencia: {}\nNumero: {}'\
            .format(self.getCliente(),self.getGerente(),self.getSaldo(),self.getAgencia(),self.getNumero())

class Pessoa():
    def __init__(self,nome,anonas,estado):
        self.__nome = nome
        self.__anonas = anonas
        self.__estado = estado
        self.__contas = []
        self.__saldototal = 0

    def getNome(self):
        return self.__nome
    def getNascimento(self):
        return self.__anonas
    def getEstado(self):
        return self.__estado
    def getContas(self):
        return self.__contas

    def getSaldoTotal(self):
        soma = 0
        for i in self.__contas:
            soma += i.getSaldo()
        return soma
    def addConta(self,x):
        self.__contas.append(x)

    def __repr__(self):
        return 'Cliente: {}\nQtde de contas: {}\nSaldo total: {}'\
            .format(self.getNome(),len(self.getContas()),self.getSaldoTotal())

class Gerente(Pessoa):
    def __init__(self,nome,registro,anonas,estado):
        super().__init__(nome,anonas,estado)
        self.__registro = registro
        self.__contas = []

    def getReg(self):
        return self.__registro
    def get(self):
        return self.__contas

    def __repr__(self):
        return 'Gerente: {}, Qtde de contas'

con0 = Conta('abcd','abc')
pes0 = Pessoa('thiago','28042000','sc')
ger0 = Gerente('leonardo','1234','12031999','sp')
con0.setGerente(ger0)
pes0.addConta(con0)
con0.deposito(1000)
con0.deposito(50)
con0.saque(160)
con0.saque(1000)
print(con0)
print()
con1= Conta('efgh','def')
ger1= Gerente('matheus','4567','30122001','sc')
con1.setGerente(ger1)
pes0.addConta(con1)
con1.deposito(500)
print(con1)
print()
print(pes0)