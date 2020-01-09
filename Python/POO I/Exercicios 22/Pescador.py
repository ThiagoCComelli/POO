# -*- coding: utf-8 -*-
class Pescador:
    __total , __melhor = 0,None
    def __init__(self,nome,idade):
        self.__nome = nome
        self.__idade = idade

    def pescou(self):
        self.__total += 1

    def getNome(self):
        return self.__nome
    def getIdade(self):
        return self.__idade
    def getTotal(self):
        return self.__total

def melhor():
    if bob.getTotal() > ted.getTotal() and bob.getTotal() > tom.getTotal():
        return bob.getNome()
    elif ted.getTotal() > bob.getTotal() and ted.getTotal() > tom.getTotal():
        return ted.getNome()
    else:
        return tom.getNome()
def pior():
    if bob.getTotal() < ted.getTotal() and bob.getTotal() < tom.getTotal():
        return bob.getNome()
    elif ted.getTotal() < bob.getTotal() and ted.getTotal() < tom.getTotal():
        return ted.getNome()
    else:
        return tom.getNome()

#A
bob = Pescador('Bob',20)
#B
bob.pescou()
#C
ted = Pescador('Ted',22)
#D
ted.pescou()
#E
ted.pescou()
#F
bob.pescou()
#G
tom = Pescador('Tom',43)
#H
tom.pescou()
#I
ted.pescou()
#J
print('{} {} {}'.format(bob.getNome(),bob.getIdade(),bob.getTotal()))
print('{} {} {}'.format(ted.getNome(),ted.getIdade(),ted.getTotal()))
print('{} {} {}'.format(tom.getNome(),tom.getIdade(),tom.getTotal()))
#K e L
print()
print(melhor())
print(pior())

