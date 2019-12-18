# -*- coding: utf-8 -*-
class Agenda():
    __total = []
    def __init__(self,desc,dono,cor):
        self.__desc = desc
        self.__dono = dono
        self.__cor = cor

# Arrumar formato de data
    def getQtdeCompromissos(self,x):
        tot = 0
        for i in self.__total:
            if i.getInicio() == x:
                tot += 1
        return tot

    def addCompromisso(self,x):
        id = None
        if self.__total[-1] != None:
            id = self.__total.getId()+1
        else:
            x.setId(0)
            self.__total.append(x)

    def removeCompromisso(self,x):
        for i in self.__total:
            if i.getId() == x:
                self.__total.remove(i)


class ItemAgenda():
    def __init__(self,id,data,horai,horaf):
        self.__id = id
        self.__data = data
        self.__horai = horai
        self.__horaf = horaf

    def getId(self):
        return self.__id
    def getInicio(self):
        return self.__horai
    def getFim(self):
        return self.__horaf

    def setId(self,id):
        self.__id = id

# Criar casos
