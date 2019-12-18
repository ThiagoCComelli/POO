# -*- coding: utf-8 -*-
class Rede():
    def __init__(self):
        self.__mercados = []

    def getMercados(self):
        return self.__mercados
    def getMaisFuncionarios(self):
        tot = ''
        tota = 0
        for i in self.__mercados:
            if len(i.getFuncionarios()) > tota:
                tot = i.getNome()
                tota = len(i.getFuncionarios())
        return tot
    def getSalarioMedioTudo(self):
        tot = 0
        tota = 0
        for i in self.__mercados:
            tot += i.getSalarioMedioTotal()
            tota += 1
        return tot/tota


    def addMercado(self,x):
        self.__mercados.append(x)

    def __repr__(self):
        return 'Rede De Mercados\nMais Funcionarios: {}\nSalario Medio(todos mercados): {}'\
            .format(self.getMaisFuncionarios(),self.getSalarioMedioTudo())

class Mercado():
    def __init__(self,nome):
        self.__nome = nome
        self.__funcionarios = []
        self.__prateleiras = []

    def getPreco(self):
        return self.__precoo
    def getNome(self):
        return self.__nome
    def getFuncionarios(self):
        tot = '| '
        for i in self.__funcionarios:
            tot += i.getNome()
            tot += ' | '
        return tot
    def getPrateleirasLista(self):
        print('Mercado: {}'.format(self.getNome()))
        for i in self.__prateleiras:
            print(i)
            print()
        return ''
    def getPrateleiras(self):
        tot = '| '
        for i in self.__prateleiras:
            tot += str(i.getId())
            tot += ' | '
        return tot
    def getSalarioTotal(self):
        tot = 0
        for i in self.__funcionarios:
            tot += i.getSalario()
        return tot
    def getSalarioMedioTotal(self):
        tot = 0
        tota = 0
        for i in self.__funcionarios:
            tot += i.getSalario()
            tota += 1
        return tot/tota
    def getSalarioMedioHomens(self):
        tot = 0
        tott = 0
        valores = '| '
        for i in self.__funcionarios:
            if i.getSexo() == 'masculino':
                tot += i.getSalario()
                tott += 1
                valores += str(i.getSalario())+' '
        valores += '| => '
        return valores+str(tot/tott)
    def getMaiorSalarioMulher(self):
        tot = 0
        tota = ''
        for i in self.__funcionarios:
            if i.getSexo() == 'feminino':
                if tot < i.getSalario():
                    tot = i.getSalario()
                    tota = i.getNome()
        return tota
    def getHomemMaisNovo(self):
        tot = 9999
        tota = ''
        for i in self.__funcionarios:
            if i.getSexo() == 'masculino':
                if i.getIdade() < tot:
                    tot = i.getIdade()
                    tota = i.getNome()
        return tota
    def getPrateleiraMaisCara(self):
        tot = 0
        tota = ''
        for i in self.__prateleiras:
            if i.getTotal() > tot:
                tot = i.getTotal()
                tota = i.getId()
        return tota

    def addPrateleira(self,x):
        self.__prateleiras.append(x)
    def addFuncionarios(self,x):
        self.__funcionarios.append(x)


    def __repr__(self):
        return 'Mercado: {}\nFuncionarios: {}\nId das Prateleiras: {}\nSalario Total: {}\nSalario Medio(total): {}\nSalario Medio(homens): {}\nMaior Salario(mulher): {}\nHomem Mais Novo: {}\nPrateleira Mais Cara: id({})'\
            .format(self.getNome(),self.getFuncionarios(),self.getPrateleiras(),self.getSalarioTotal(),self.getSalarioMedioTotal(),self.getSalarioMedioHomens(),self.getMaiorSalarioMulher(),self.getHomemMaisNovo(),self.getPrateleiraMaisCara())


class Funcionario():
    def __init__(self,nome,idade,sexo,salario):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo
        self.__salario = salario

    def getNome(self):
        return self.__nome
    def getIdade(self):
        return self.__idade
    def getSexo(self):
        return self.__sexo
    def getSalario(self):
        return self.__salario




class Produto():
    def __init__(self,descricao,preco=0,quantidade=0):
        self.__descricao = descricao
        self.__preco = preco
        self.__quantidade = quantidade

    def getDescricao(self):
        return self.__descricao
    def getPreco(self):
        return self.__preco
    def getQuantidade(self):
        return self.__quantidade



class Prateleira():
    def __init__(self,id):
        self.__id = id
        self.__produtos = []
        self.__nomeMaisCaro = ''
        self.__precoMaisCaro = 0
        self.__total = 0

    def getTotal(self):
        return self.__total
    def getId(self):
        return self.__id
    def getProdutos(self):
        return self.__produtos
    def getNomeMaisCaro(self):
        return self.__nomeMaisCaro
    def getPrecoMaisCaro(self):
        return self.__precoMaisCaro
    def getProdutosLista(self):
        tot = '| '
        for i in self.getProdutos():
            tot += i.getDescricao()
            tot += ' | '
        return tot
    def getEstoqueMaisCaro(self):
        tot = 0
        tota = ''
        for i in self.getProdutos():
            if tot < i.getPreco()*i.getQuantidade():
                tot = i.getPreco()*i.getQuantidade()
                tota = i.getDescricao()
        return tota

    def addProduto(self,x):
        self.__produtos.append(x)
        self.__total += x.getPreco()*x.getQuantidade()
        if x.getPreco() > self.__precoMaisCaro:
            self.__nomeMaisCaro = x.getDescricao()
            self.__precoMaisCaro = x.getPreco()
    def removeProduto(self,x):
        self.__produtos.remove(x)

    def __repr__(self):
        return 'Prateleira Id: {}\nProdutos: {}\nProduto Mais Caro: {}\nEstoque Mais Caro: {}'\
            .format(self.getId(),self.getProdutosLista(),self.getNomeMaisCaro(),self.getEstoqueMaisCaro())

mer0 = Mercado('mer0')
mer1 = Mercado('mer1')
fun0 = Funcionario('thiago',19,'masculino',1900)
fun1 = Funcionario('lucas',23,'masculino',2000)
fun2 = Funcionario('fran',18,'feminino',2100)
fun3 = Funcionario('ana',17,'feminino',2200)
pra0 = Prateleira(0)
pra01 = Prateleira(1)
pra1 = Prateleira(2)
pro0 = Produto('pera',10,3)
pro01 = Produto('maca',12,2)
pro02 = Produto('banana',19,1)
pro03 = Produto('goiaba',9,3)
pro04 = Produto('melancia',7,10)
mer0.addFuncionarios(fun0)
mer0.addFuncionarios(fun1)
mer0.addFuncionarios(fun2)
mer0.addFuncionarios(fun3)
mer1.addFuncionarios(fun0)
mer1.addFuncionarios(fun2)

pra0.addProduto(pro0)
pra0.addProduto(pro01)
pra01.addProduto(pro04)
pra01.addProduto(pro02)
pra01.addProduto(pro03)
pra1.addProduto(pro0)
pra1.addProduto(pro03)

mer0.addPrateleira(pra0)
mer0.addPrateleira(pra01)
mer1.addPrateleira(pra1)

rede = Rede()
rede.addMercado(mer0)
rede.addMercado(mer1)

print(mer0)
print()
print(mer1)
print()
print(rede)
print()
print(mer0.getPrateleirasLista())
print()
print(mer1.getPrateleirasLista())

