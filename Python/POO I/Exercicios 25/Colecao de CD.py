# -*- coding: utf-8 -*-
cdide = []
class Cd():
    def __init__(self,capm,titulo,ide):
        self.__capm = capm
        self.__titulo = titulo
        self.__ide = ide
        self.__musicas = []
        self.__banda = None
        self.__cap = 0
        self.__maisLonga = ''
        self.__maisCurta = ''
        self.__maisEspaco = ''

    def getMusicas1(self):
        return self.__musicas
    def getCapm(self):
        return self.__capm
    def getTitulo(self):
        return self.__titulo
    def getId(self):
        return self.__ide
    def getNomeBanda(self):
        return self.__banda
    def getMusicas(self):
        return len(self.__musicas)
    def getLisMusicas(self):
        tot = ''
        for i in self.__musicas:
            tot += i + ' | '
        return tot
    def getCapa(self):
        tot = self.getCapm()-self.__cap
        return tot
    def getCap(self):
        return self.__cap
    def getPerCap(self):
        return (self.getCap()/self.getCapm())*100

    def getMaisCurta(self):
        return self.__maisCurta

    def setBanda(self,x):
        self.__banda = x.getNomeDaBanda()
    def setMusica(self,x):
        if x.getTamanho() + self.__cap <= self.__capm:
            self.__musicas.append(x.getNome())
            self.__cap += x.getTamanho()





    def __repr__(self):
        return 'Titulo: {}, Banda: {}, Capacidade: {}, Id: {}, Qtde Musicas: {}, Lista de Musicas: {}, Espaco Livre: {} MB, Espaco Ocupado: {} MB, Espaco Ocupado: {:.0f}%'\
            .format(self.getTitulo(),self.getNomeBanda(),self.getCapm(),self.getId(),self.getMusicas(),self.getLisMusicas(),self.getCapa(),self.getCap(),self.getPerCap())



class Musica():
    def __init__(self,nome,dura,tamanho):
        self.__nome = nome
        self.__dura = dura
        self.__tamanho = tamanho

    def getNome(self):
        return self.__nome
    def getDura(self):
        return self.__dura
    def getTamanho(self):
        return self.__tamanho

    def __repr__(self):
        return 'Musica: {} | Duracao: {} | Tamanho: {}'\
            .format(self.getNome(),self.getDura(),self.getTamanho())


class Pessoa():
    def __init__(self,nome):
        self.__nome = nome
        self.__cds = []
        self.__musicas = []

    def getNome(self):
        return self.__nome
    def getQtdeCds(self):
        return len(self.__cds)
    def getQtdeMusicas(self):
        return len(self.__musicas)

    def addCds(self,x):
        self.__cds.append(x.getTitulo())
        self.__musicas.append(x.getMusicas())
    def removeCds(self,x):
        self.__cds.remove(x.getTitulo())
        self.__musicas.remove(x.getMusicas())


    def __repr__(self):
        return 'Pessoa: {}, Qtde de Cds: {}, Qtde de Musicas: {}'.format(self.getNome(),self.getQtdeCds(),self.getQtdeMusicas())


class Cantor(Pessoa):
    def __init__(self,nome):
        super().__init__(nome)

    def __repr__(self):
        return 'Cantor: {}'.format(self.getNome())

class Banda():
    def __init__(self,nomedabanda):
        self.__nomedabanda = nomedabanda
        self.__cantores = []

    def getNomeDaBanda(self):
        return self.__nomedabanda
    def addCantor(self,x):
        self.__cantores.append(x.getNome())
    def getCantores(self):
        tot = ''
        for i in self.__cantores:
            tot += (i + ' | ')
        return tot

    def __repr__(self):
        return 'Participantes da Banda = {}'.format(self.getCantores())

#0 Cria Album
#1 Cria Banda
#2 Adiciona Cantores à banda
#3 Vincula uma banda à algum album
#4 Adiciona um Cd a lista de alguem

cd0 = Cd(1000,'Altos',0)
cd1 = Cd(900,'Baixos',1)

mus0 = Musica('alura',100,120)
mus1 = Musica('aluraasas',140,190)
mus2 = Musica('aluraas121213as',1400,100)
mus3 = Musica('alu',150,105)
mus4 = Musica('aluraa',140,120)

pes0 = Pessoa('Thiago')
pes1 = Pessoa('lucas')

cant0 = Cantor('Slash')
cant1 = Cantor('Bob')
cant2 = Cantor('Clinton')

ban0 = Banda('Banda0')
ban0.addCantor(cant0)
ban0.addCantor(cant1)

ban1 = Banda('Banda1')
ban1.addCantor(cant2)

cd0.setBanda(ban0)
cd1.setBanda(ban1)


cd0.setMusica(mus0)
cd1.setMusica(mus1)
cd1.setMusica(mus2)
cd0.setMusica(mus3)
cd1.setMusica(mus4)

print(cd0)
print(cd1)
print()
pes0.addCds(cd0)
pes0.addCds(cd1)
pes1.addCds(cd0)
print(pes0)
print(pes1)
pes0.removeCds(cd0)
print()
print(pes0)
print(pes1)
print()


