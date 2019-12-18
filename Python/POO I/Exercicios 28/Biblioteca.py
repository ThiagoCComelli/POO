# -*- coding: utf-8 -*-
class Biblioteca():
    def __init__(self,nome,cap):
        self.__nome = nome
        self.__cap = cap
        self.__prateleira = []
        self.__bibliotecarios = []
        self.__clientes = []

    def getNome(self):
        return self.__nome
    def getCap(self):
        return self.__cap
    def getPrateleiras(self):
        return self.__prateleira
    def getBibliotecarios(self):
        return self.__bibliotecarios
    def getClientes(self):
        return self.__clientes

    def getMediaSalario(self):
        maisantigo = None
        for i in self.__bibliotecarios:
            if maisantigo == None:
                maisantigo = i.getAdmissao()
            else:
                if maisantigo > i.getAdmissao():
                    maisantigo = i.getAdmissao()
        tot = 0
        tota = 0
        for i in self.__bibliotecarios:
            if i.getAdmissao() == maisantigo:
                tot += 1
                tota += i.getSalario()
        return tota/tot

    def getDrama(self):
        tot = ''
        for i in self.__prateleira:
            if i.getCategoria() == 'drama':
                tot += i.getLivros()
        return tot

    def getIdadeMediaClientes(self):
        tot = 0
        tota = 0
        for i in self.__clientes:
            tot += 1
            tota += i.getIdade()
        return tota/tot

    def prateleiras(self):
        print('Biblioteca: {}\n'.format(self.getNome()))
        for i in self.__prateleira:
            print(i)
            print()
        return ''

    def getPrecoMaisCaro(self):
        tot = 0
        for i in self.__prateleira:
            for j in i.getLivross():
                if j.getPreco() > tot:
                    tot = j.getPreco()
        return tot

    def addPrateleira(self,x):
        self.__prateleira.append(x)
    def addBibliotecario(self,x):
        self.__bibliotecarios.append(x)
    def addCliente(self,x):
        self.__clientes.append(x)


    def __repr__(self):
        return 'Biblioteca {}\nMedia Salarial(mais antigo): {}\nLivros de Drama: {}\nIdade Media Dos Clientes: {}\nPreco do Livro Mais Caro: {}\n'\
            .format(self.getNome(),self.getMediaSalario(),self.getDrama(),self.getIdadeMediaClientes(),self.getPrecoMaisCaro())

class Prateleira():
    def __init__(self,id,categoria):
        self.__id = id
        self.__categoria = categoria
        self.__livros = []
        self.__precomaiscaro = 0

    def getPrecoMaisCaro(self):
        return self.__precomaiscaro
    def getId(self):
        return self.__id
    def getCategoria(self):
        return self.__categoria
    def getLivross(self):
        return self.__livros
    def getLivros(self):
        tot = '| '
        for i in self.__livros:
            tot += i.getNome()
            tot += ' | '
        return tot

    def addLivro(self,x):
        if x.getCategoria() == self.getCategoria():
            self.__livros.append(x)
        else:
            return False

    def precoTotal(self):
        tot = 0
        for i in self.__livros:
            tot += i.getPreco()
        return tot

    def maisCaro(self):
        tot = 0
        tota = ''
        for i in self.__livros:
            if i.getPreco() > tot:
                tot = i.getPreco()
                tota = i.getNome()
        self.__precomaiscaro = tot
        return tota

    def __repr__(self):
        return 'Prateleira: id({})\nCategoria: {}\nLivros: {}\nPreco Total: {}\nLivro Mais Caro: {}'\
            .format(self.getId(),self.getCategoria(),self.getLivros(),self.precoTotal(),self.maisCaro())

class Livro():
    def __init__(self,ano,autor,categoria,paginas,nome,preco):
        self.__ano = ano
        self.__autor = autor
        self.__categoria = categoria
        self.__paginas = paginas
        self.__nome = nome
        self.__preco = preco

    def getAno(self):
        return self.__ano
    def getAutor(self):
        return self.__autor
    def getCategoria(self):
        return self.__categoria
    def getPaginas(self):
        return self.__paginas
    def getNome(self):
        return self.__nome
    def getPreco(self):
        return self.__preco

class Pessoa():
    def __init__(self,nome,idade):
        self.__nome = nome
        self.__idade = idade

    def getNome(self):
        return self.__nome
    def getIdade(self):
        return self.__idade

class Bibliotecario(Pessoa):
    def __init__(self,nome,idade,admissao,salario):
        super().__init__(nome,idade)
        self.__admissao = admissao
        self.__salario = salario

    def getAdmissao(self):
        return int(self.__admissao[-4:])
    def getSalario(self):
        return self.__salario

class Cliente(Pessoa):
    def __init__(self,nome,idade,endereco):
        super().__init__(nome,idade)
        self.__endereco = endereco

    def getEndereco(self):
        return self.__endereco



pes0 = Cliente('thiago',19,'88130-485')
pes1 = Cliente('ana',17,'88130-486')
pes2 = Bibliotecario('fran',24,'28 04 2000',1200)
pes3 = Bibliotecario('lucas',25,'28 04 1997',2100)
pes4 = Bibliotecario('maicon',25,'28 04 1997',1000)

bib0 = Biblioteca('bib0',100)

liv0 = Livro('2000','autor1','drama','1000','alemdisso',100)
liv1 = Livro('2000','autor2','drama','1000','asd',1010)
liv2 = Livro('2000','autor2','acao','1000','qwe',1001)
liv3 = Livro('2000','autor1','terror','1000','fre',11010)
liv4 = Livro('2000','autor1','terror','1000','gre',110)
liv5 = Livro('2000','autor1','drama','1000','gwaz',11200)
liv6 = Livro('2000','autor1','terror','1000','csa',10)
liv7 = Livro('2000','autor1','terror','1000','zcs',112300)

pra0 = Prateleira(0,'drama')
pra1 = Prateleira(1,'acao')
pra2 = Prateleira(2,'terror')

pra0.addLivro(liv0)
pra0.addLivro(liv1)
pra0.addLivro(liv5)

pra1.addLivro(liv2)

pra2.addLivro(liv3)
pra2.addLivro(liv4)
pra2.addLivro(liv6)
pra2.addLivro(liv7)

bib0.addPrateleira(pra0)
bib0.addPrateleira(pra1)
bib0.addPrateleira(pra2)

bib0.addBibliotecario(pes2)
bib0.addBibliotecario(pes3)
bib0.addBibliotecario(pes4)
bib0.addCliente(pes0)
bib0.addCliente(pes1)

print(bib0)
print()
print(bib0.prateleiras())
