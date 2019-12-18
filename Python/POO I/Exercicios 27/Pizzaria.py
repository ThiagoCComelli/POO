# -*- coding: utf-8 -*-
menu = {}
class Grupo():
    def __init__(self):
        self.__pessoas = []

    def addPessoa(self,x):
        self.__pessoas.append(x)
    def getMaisCaroGeral(self):
        tot = 0
        tota = ''
        for i in self.__pessoas:
            for j in i.getComanda:
                if j.getMaisCaroV() > tot:
                    tota = j.getMaisCaro()
                    tot = j.getMaisCaroV()
        return tota

    def __repr__(self):
        return 'Produto mais caro geral: {}'\
            .format(self.getMaisCaroGeral())

class Pessoa():
    def __init__(self,nome):
        self.__nome = nome
        self.__comanda = None

    def getNome(self):
        return self.__nome
    def getComanda(self):
        return self.__comanda

    def addComanda(self,x):
        self.__comanda = x
    def pedido(self,x,y):
        self.__comanda.pedido(x,y)


class Comanda():
    def __init__(self,data,id):
        self.__data = data
        self.__id = id
        self.__itensconsumo = []
        self.__valor = 0
        self.__maisCaro = ''
        self.__maisCarov = 0

    def getMaisCaro(self):
        return self.__maisCaro
    def getMaisCaroV(self):
        return self.__maisCarov
    def getId(self):
        return self.__id
    def getData(self):
        return self.__data
    def getConsumo(self):
        tot = '| '
        if len(self.__itensconsumo) > 0:
            for i in self.__itensconsumo:
                tot += i
                tot += ' | '
        return tot
    def getValor(self):
        return self.__valor
    def pedido(self,x,y):
        for i in range(y):
            self.__itensconsumo.append(x)
            self.__valor += menu[x]
        if menu[x] > self.__maisCarov:
            self.__maisCarov = menu[x]
            self.__maisCaro = x

    def __repr__(self):
        return 'Comanda id: {} Data: {}\nConsumo: {}\nValor: {}'\
            .format(self.getId(),self.getData(),self.getConsumo(),self.getValor())


'''
class Menu():
    def __init__(self):
        self.__itens = {}

    def getItens(self):
        return self.__itens
    def getItensX(self,x):
        return self.__itens[x]

    def addItens(self,x,y):
        self.__itens[x] = y
'''

class Produto():
    def __init__(self,descricao,valor):
        self.__descricao = descricao
        self.__valor = valor

    def getDescricao(self):
        return self.__descricao
    def getValor(self):
        return self.__valor

grupo = Grupo()
pes = Pessoa('thiago')
pes1 = Pessoa('lucas')
com = Comanda('12/01',0)
com1 = Comanda('12/01',1)
pes.addComanda(com)
pes1.addComanda(com1)

pizza = Produto('pizza',60)
batata = Produto('batata',30)
refri = Produto('refri',10)
coracao = Produto('coracao',40)
pastel = Produto('pastel',5)
camarao = Produto('camarao',120)
menu[pizza.getDescricao()] = pizza.getValor()
menu[batata.getDescricao()] = batata.getValor()
menu[refri.getDescricao()] = refri.getValor()
menu[coracao.getDescricao()] = coracao.getValor()
menu[pastel.getDescricao()] = pastel.getValor()
menu[camarao.getDescricao()] = camarao.getValor()
pes.pedido('pizza',3)
pes1.pedido('camarao',1)
pes1.pedido('refri',1)

print(pes.getComanda())
print()
print(pes1.getComanda())
print()
print(grupo)
