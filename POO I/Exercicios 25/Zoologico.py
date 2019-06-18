# -*- coding: utf-8 -*-
class Zoologico():
    def __init__(self,nome='',jaulas=[],tratadores=[],animais=[]):
        self.__nome = nome
        self.__jaulas = jaulas
        self.__tratadores = tratadores
        self.__animais = animais

    def getNome(self):
        return self.__nome
    def getJaulas(self):
        tot = 0
        for i in self.__jaulas:
            tot += 1
        return tot
    def getTratadores(self):
        tot = 0
        for i in self.__tratadores:
            tot += 1
        return tot
    def getAnimais(self):
        tot = 0
        for i in self.__jaulas:
            tot += 0
        return tot
    def getZooTotalAnimais(self):
        tot = 0
        for i in self.__jaulas:
            tot += self.__jaulas.getCapacidade
    def setTratadores(self,x):
        self.__tratadores.append(x)
    def setNovaJaula(self,j):
        if len(self.__jaulas) > 0:
            j.setId(self.__jaulas[-1].getId()+1)
        self.__jaulas.append(j)

    def __repr__(self):
        return 'Nome do Zoo: {}\nTotal de Jaulas: {}\nTotal de Tratadores: {}\nTotal de Animais: {}\nCapacidade maxima: '\
            .format(self.getNome(),self.getJaulas(),self.getTratadores(),self.getAnimais())

class Jaula():
    def __init__(self,comprimento,largura,capacidademax,id):
        self.__comprimento = comprimento
        self.__largura = largura
        self.__capacidademax = capacidademax
        self.__id = id
        self.__animais = []

    def getArea(self):
        return self.__comprimento*self.__largura
    def getCapacidade(self):
        return self.__capacidademax
    def getId(self):
        return self.__id
    def getQtde(self):
        return len(self.__animais)
    def getAnimalMaisVelho(self):
        if len(self.__animais) > 0:
            mais_velho = self.__animais[-1]
            for a in range(0, len(self.__animais) - 1):
                if self.__animais[a].getIdade() > mais_velho.getIdade():
                    mais_velho = self.__animais[a]
            return mais_velho
        else:

            return mais
    def setId(self,id):
        self.__id = id
    def setAnimal(self,animal):
        if len(self.__animais) > 0:
            ver = self.__animais[-1]
            if animal.getTipo() == self.__animais[-1].getTipo():
                self.__animais.append(animal)
            else:
                return 'tipos diferentes'
        else:
            self.__animais.append(animal)
    def __repr__(self):
        return 'Jaula: {}\nArea: {}\nCapacidade maxima: {}\nTotal de Animais: {}\nAnimal mais velho: {}'\
            .format(self.getId(),self.__largura*self.__comprimento,self.getCapacidade(),self.getQtde(),self.getAnimalMaisVelho())

class Animal():
    def __init__(self,nome,idade,peso,especie,tipo):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__tipo = tipo
        self.__especie = especie

    def getNome(self):
        return self.__nome
    def getIdade(self):
        return self.__idade
    def getPeso(self):
        return self.__peso
    def getTipo(self):
        return self.__tipo
    def getEspecieA(self):
        return self.__especie


class Tratador():
    def __init__(self,nome,idade,animais):
        self.__nome = nome
        self.__idade = idade
        self.__animais = animais

    def getAnimais(self):
        return self.__animais
    def getNome(self):
        return self.__nome
    def getIdade(self):
        return self.__idade

trat0 = Tratador('ricardo',34,'herbivoro')
trat1 = Tratador('ricardo1',341,'carnivoro')
trat2 = Tratador('ricardo2',342,'onivoro')
urso = Animal('urso0',12,32,'urso','onivoro')
urso1 = Animal('urso1',12,32,'urso','onivoro')
jaula0 = Jaula(10,100,10,0)
jaula0.setAnimal(urso)
jaula0.setAnimal(urso1)
zoo0 = Zoologico('zoo0')
zoo0.setTratadores(trat0)
zoo0.setTratadores(trat1)
zoo0.setNovaJaula(jaula0)

print(zoo0)
print()
print(jaula0)
'''
trat3 = Tratador('lucio',34,'herbivoro')
trat4 = Tratador('lucio1',334,'carnivoro')
trat5 = Tratador('lucio2',344,'herbivoro')
zoo1 = Zoologico('zoo1')
hiena = Animal('hiena0',34,3232,'hiena','carnivoro')
zoo1.setTratadores(trat4)
jaula01 = Jaula(10,200,10,1)
print(zoo1)
print()
'''
'''
NAO TA PRONTO
TEM QUE ALTERAR A PORRA TODA
NAO TA PRONTO
TEM QUE ALTERAR A PORRA TODA
NAO TA PRONTO
TEM QUE ALTERAR A PORRA TODA
NAO TA PRONTO
TEM QUE ALTERAR A PORRA TODA
NAO TA PRONTO
TEM QUE ALTERAR A PORRA TODA
'''