# -*- coding: utf-8 -*-
class Zoologico():
    def __init__(self,nome,jaulas,tratadores,animais):
        self.__nome = nome
        self.__jaulas = jaulas
        self.__tratadores = tratadores
        self.__animais = animais

    def getNome(self):
        return self.__nome
    def getJaulas(self):
        return self.__jaulas
    def getTratdores(self):
        return self.__tratadores
    def getAnimais(self):
        return self.__animais

    def setNovaJaula(self,j):
        if len(self.__jaulas) > 0:
            j.setId(self.__jaulas[-1].getId()+1)
        self.__jaulas.append(j)

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
        mais = self.__animais[-1]
        if len(self.__animais)>0:
            for i in self.__animais:
                if i.getIdade() > mais.getIdade:
                    mais = i
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



class Animal()
    def __init__(self,nome,idade,peso,tipo,especie):
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





