# -*- coding: utf-8 -*-
class Computador:
    def __init__(self,basico = 0,windows = False, linux = False, neon = False):
        self.__basico = basico
        self.__windows = windows
        self.__linux = linux
        self.__neon = neon

    def getWindows(self):
        return self.__windows
    def getLinux(self):
        return self.__linux
    def getNeon(self):
        return self.__neon
    def getBasico(self):
        return self.__basico

    def setWindows(self,windows):
        self.__windows = windows
    def setLinux(self,linux):
        self.__linux = linux
    def setNeon(self,neon):
        self.__neon = neon
    def setBasico(self,basico):
        self.__basico = basico

    def precoTotal(self):
        total = self.__basico
        t = ''
        if self.__windows == True:
            total += 500
            t += 'Windows '
        if self.__linux == True:
            total += 2
            t += 'Linux '
        if self.__neon == True:
            total += 100
            t += 'Neon '
        return total,t
#A
c = Computador(2000)
#B
c.setWindows(True)
c.setNeon(True)
#C
c1 = Computador(2500)
#D
c1.setLinux(True)
#E
c2 = Computador(1500)
#F
#G
print(*c.precoTotal())
print(*c1.precoTotal())
print(*c2.precoTotal())




