# -*- coding: utf-8 -*-
class UrnaEletronica:
    __status = 0
    __estado = 2
    def __init__(self,total = 0,zak = 0, tonim = 0, asdrubol = 0, branco = 0, nulo = 0):
        self.__total = total
        self.__zak  = zak
        self.__tonim = tonim
        self.__asdrubol = asdrubol
        self.__branco = branco
        self.__nulo = nulo

    def setLigar(self):
        self.__status = 1
    def setDesligar(self):
        self.__status = 0
        self.__total = 0
        self.__zak = 0
        self.__tonim = 0
        self.__asdrubol = 0
        self.__branco = 0
        self.__nulo = 0
        self.__estado = 2
    def setEncerrar(self):
        self.__estado = 0
    def setIniciar(self):
        self.__estado = 1
    def getStatus(self):
        if self.__status == 1:
            return 'ligada'
        elif self.__status == 0:
            return 'desligada'
    def getEstado(self):
        if self.__estado == 0:
            return 'encerrada'
        elif self.__estado == 1:
            return 'iniciada'
        elif self.__estado == 2:
            return 'nao iniciada'

    def getZak(self):
        return self.__zak
    def getTonim(self):
        return self.__tonim
    def getAsdrubol(self):
        return self.__asdrubol
    def getTotal(self):
        return self.__total
    def getNulos(self):
        return self.__nulo
    def getBrancos(self):
        return self.__branco


    def votar(self,codigo):
        if self.__status == 1 and self.__estado == 1:
            self.__total += 1
            if codigo == 54:
                self.__zak += 1
            elif codigo == 67:
                self.__asdrubol += 1
            elif codigo == 83:
                self.__tonim += 1
            elif codigo == 0:
                self.__branco += 1
            else:
                self.__nulo += 1
        else:
            return False

def getNulos1():
    return um.getNulos()+dois.getNulos()+tres.getNulos()
def getBrancos1():
    return um.getBrancos()+dois.getBrancos()+tres.getBrancos()
def getTotal1():
    return um.getTotal()+dois.getTotal()+tres.getTotal()
def getZak1():
    return um.getZak() + dois.getZak() + tres.getZak()
def getTonim1():
    return um.getTonim() + dois.getTonim() + tres.getTonim()
def getAsdrubol1():
    return um.getAsdrubol() + dois.getAsdrubol() + tres.getAsdrubol()
def getVencedor():
    if getZak1() > getAsdrubol1() and getZak1() > getTonim1():
        return 'Zak {:.1f}%'.format((getZak1()/getTotal1())*100)
    elif getTonim1() > getAsdrubol1() and getTonim1() > getZak1():
        return 'Tonim {:.1f}%'.format((getTonim1()/getTotal1())*100)
    else:
        return 'Asdrubol {:.1f}%'.format((getAsdrubol1()/getTotal1())*100)



#1
um = UrnaEletronica()
dois = UrnaEletronica()
tres = UrnaEletronica()
#2
um.setLigar()
dois.setLigar()
tres.setLigar()
#3
print(um.getStatus())
#4
print(dois.getEstado())
#5
tres.votar(54)
#6
print(tres.getTotal())
#7
um.setIniciar()
dois.setIniciar()
tres.setIniciar()
#8
tres.votar(54)
#9
um.votar(0)
#10
um.votar(67)
#11
tres.votar(0)
#12
um.votar(0)
#13
um.votar(12)
#14
um.votar(83)
#15
dois.votar(83)
#16
dois.votar(0)
#17
tres.votar(67)
#18
dois.votar(54)
#19
tres.votar(83)
#20
tres.votar(0)
#21
dois.votar(67)
#22
tres.votar(83)
#23
tres.votar(32)
#24
um.votar(54)
#25
tres.votar(83)
#26
tres.votar(0)
#27
dois.votar(98)
#28
tres.votar(67)
#29
dois.votar(10)
#30
dois.votar(54)
#31
tres.votar(83)
#32
dois.setDesligar()
#33
dois.votar(83)
#34
dois.setLigar()
#35
dois.votar(83)
#36
dois.setIniciar()
#37
dois.votar(83)
#38
um.setEncerrar()
dois.setEncerrar()
tres.setEncerrar()
#39
dois.votar(83)
#40
print('1 = {} {} {} {} {}'.format(um.getZak(),um.getAsdrubol(),um.getTonim(),um.getBrancos(),um.getNulos()))
print('2 = {} {} {} {} {}'.format(dois.getZak(),dois.getAsdrubol(),dois.getTonim(),dois.getBrancos(),dois.getNulos()))
print('3 = {} {} {} {} {}'.format(tres.getZak(),tres.getAsdrubol(),tres.getTonim(),tres.getBrancos(),tres.getNulos()))
#41
print(getTotal1())
#42
print(getTotal1()-getBrancos1()-getNulos1())
#43
print('{} {:.1f}%'.format(getNulos1(),(getNulos1()/getTotal1())*100))
#44
print('{} {:.1f}%'.format(getBrancos1(),(getBrancos1()/getTotal1())*100))
#45
print('Zak = {}   Asdrubol = {}   Tonim = {}   Vencedor = {} '.format(getZak1(),getAsdrubol1(),getTonim1(),getVencedor()))
