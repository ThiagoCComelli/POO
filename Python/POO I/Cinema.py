# -*- coding: utf-8 -*-
class Cinema():
    def __init__(self,nome,endereco):
        self.__nome = nome
        self.__endereco = endereco
        self.__funcionarios = []
        self.__salas = []
        self.__filmes = []
        self.__sessoes = []

    def getNome(self):
        return self.__nome
    def getEndereco(self):
        return self.__endereco
    def getFuncionarios(self):
        return self.__funcionarios
    def getSalas(self):
        return self.__salas
    def getFilmes(self):
        return self.__sessoes
    def getSessaoMaisCara(self):
        maior = 0
        nome = 0
        for i in self.__sessoes:
            if i.getPreco() > maior:
                maior = i.getPreco()
                nome = i.getLocal()
        return 'Sessao mais cara(preco): R$ {}  Local(sala): {}'.format(str(maior),str(nome))
    def getFilmeComedia(self):
        filmes = 'Filmes de Comédia no Cinema: '
        for i in self.__filmes:
            if i.getGenero() == 'comedia':
                filmes += i.getNome()
                filmes += ' | '
        return filmes
    def getGeneroMaisFrequente(self):
        lista = []
        for i in self.__sessoes:
            a = i.getFilmee()
            lista.append(a.getGenero())
        lista1 = set(lista)

        genero = ''
        count = 0
        for i in lista1:
            if lista.count(i) > count:
                genero = i
                count = lista.count(i)
        return 'Genero Mais Frequente Nas Sessoes: {}'.format(genero)
    def getMaiorLucro(self):
        maior = 0
        for i in self.__sessoes:
            preco = i.getPreco()
            sala = i.getLocall()
            cap = sala.getCap()
            tot = cap*preco
            if tot>maior:
                maior = tot
        return 'Maior Lucro Possivel Sera de: R$ {}'.format(maior)

    def setSessao(self,x):
        self.__sessoes.append(x)
    def setSala(self,x):
        self.__salas.append(x)
    def setFilme(self,x):
        self.__filmes.append(x)
    def setFuncionario(self,x):
        self.__funcionarios.append(x)

class Pessoa():
    def __init__(self,nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

class Diretor(Pessoa):
    def __init__(self,nome):
        super().__init__(nome)

    def getNome(self):
        return self.__nome

class Funcionario(Pessoa):
    def __init__(self,nome,idade,salario,sexo):
        super().__init__(nome)
        self.__idade = idade
        self.__salario = salario
        self.__sexo = sexo

    def getNome(self):
        return self.__nome
    def getIdade(self):
        return self.__idade
    def getSalario(self):
        return self.__salario
    def getSexo(self):
        return self.__sexo

class Sala():
    def __init__(self,id,cap):
        self.__id = id
        self.__cap = cap

    def getId(self):
        return self.__id
    def getCap(self):
        return self.__cap


class Filme():
    def __init__(self,nome,lancamento,diretor,genero,duracao):
        self.__nome = nome
        self.__lancamento = lancamento
        self.__diretor = diretor
        self.__genero = genero
        self.__duracao = duracao

    def getNome(self):
        return self.__nome
    def getLancamento(self):
        return self.__lancamento
    def getDiretor(self):
        return self.__diretor
    def getGenero(self):
        return self.__genero
    def getDuracao(self):
        return self.__duracao

class Sessao():
    def __init__(self,inicio,preco):
        self.__inicio = inicio
        self.__preco = preco
        self.__local = ''
        self.__filme = ''

    def getIncio(self):
        return self.__inicio
    def getLocal(self):
        return self.__local.getId()
    def getLocall(self):
        return self.__local
    def getPreco(self):
        return self.__preco
    def getFilme(self):
        return self.__filme.getNome()
    def getFilmee(self):
        return self.__filme

    def setFilme(self,x):
        self.__filme = x
    def setLocal(self,x):
        self.__local = x

    def __repr__(self):
        return 'Incio: {}\nPreco: {}\nLocal(sala): {}\nFilme: {}'.format(self.getIncio(),self.getPreco(),self.getLocal(),self.getFilme())

cine0 = Cinema('cine0','88130-000')
func0 = Funcionario('thiago',19,1900,'masculino')
dire0 = Diretor('lorenzo')
film0 = Filme('film0','08/2019',dire0,'comedia',130)
film1 = Filme('film1','08/2012',dire0,'acao',120)
film2 = Filme('film2','08/2011',dire0,'comedia',90)
film3 = Filme('film3','08/2014',dire0,'terror',200)
film4 = Filme('film4','08/2015',dire0,'suspense',100)
film5 = Filme('film5','08/2016',dire0,'comedia',45)
sala0 = Sala(0,100)
sala1 = Sala(1,101)
sala2 = Sala(2,102)
sala3 = Sala(3,103)
sala4 = Sala(4,104)
sala5 = Sala(5,105)
sess0 = Sessao('28/04/3010 - 13:30',12)
sess1 = Sessao('28/04/3011 - 13:30',20)
sess2 = Sessao('28/04/3012 - 13:30',18)
sess3 = Sessao('28/04/3013 - 13:30',121)
sess4 = Sessao('28/04/3014 - 13:30',32)
sess5 = Sessao('28/04/3015 - 13:30',122)
cine0.setFuncionario(func0)

sess0.setFilme(film0)
sess1.setFilme(film1)
sess2.setFilme(film2)
sess3.setFilme(film3)
sess4.setFilme(film4)
sess5.setFilme(film5)

sess0.setLocal(sala0)
sess1.setLocal(sala1)
sess2.setLocal(sala2)
sess3.setLocal(sala3)
sess4.setLocal(sala4)
sess5.setLocal(sala5)

cine0.setFilme(film0)
cine0.setFilme(film1)
cine0.setFilme(film2)
cine0.setFilme(film3)
cine0.setFilme(film4)
cine0.setFilme(film5)

cine0.setSessao(sess0)
cine0.setSessao(sess1)
cine0.setSessao(sess2)
cine0.setSessao(sess3)
cine0.setSessao(sess4)
cine0.setSessao(sess5)

cine0.setSala(sala0)
cine0.setSala(sala1)
cine0.setSala(sala2)
cine0.setSala(sala3)
cine0.setSala(sala4)
cine0.setSala(sala5)

print(cine0.getSessaoMaisCara())
print()
print(cine0.getFilmeComedia())
print()
print(cine0.getGeneroMaisFrequente())
print()
print(cine0.getMaiorLucro())