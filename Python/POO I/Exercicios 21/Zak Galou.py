# -*- coding: utf-8 -*-
class Personagem:
    def __init__(self,nome,vidam,velocidadem,x,y):
        self.__nome = nome
        self.__vidam = vidam
        self.__velocidadem = velocidadem
        self.__x = x
        self.__y = y

    def mover(self,direcao,velocidade):
        print(self.__x,self.__y)
        if velocidade <= self.__velocidadem and velocidade > 0:
            if direcao == 'l':
                self.__x += velocidade
            elif direcao == 'o':
                self.__x -= velocidade
            elif direcao == 'n':
                self.__y += velocidade
            elif direcao == 's':
                self.__y -= velocidade
        else:
            return False
        print(self.__x,self.__y)

    def getNome(self):
        return self.__nome
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getVelocidadem(self):
        return self.__velocidadem
    def getVida(self):
        return self.__vidam

def colide(a,b):
    if a.getX() == b.getX() and a.getY() == b.getY():
        print('colide')
    else:
        print('nao colide')
def distancia(a,b):
    x = abs(a.getX() - b.getX()) + abs(a.getY() - b.getY())
    return x


#1
zak = Personagem('Zak',125,10,2,27)
#2
galou = Personagem('Galou',100,7,29,6)
#3
tonim = Personagem('Tonim',150,4,20,8)
#4
zak.mover('l',7)
#5
zak.mover('l',10)
#6
zak.mover('l',10)
#7
zak.mover('s',5)
#8
zak.mover('n',20)
#9
galou.mover('n',2)
#10
galou.mover('n',0)
#11
galou.mover('n',7)
#12
galou.mover('n',7)
#13
tonim.mover('o',3)
#14
print('{} {} {} {} {}'.format(zak.getNome(),zak.getVelocidadem(),zak.getVida(),zak.getX(),zak.getY()))
print('{} {} {} {} {}'.format(galou.getNome(),galou.getVelocidadem(),galou.getVida(),galou.getX(),galou.getY()))
print('{} {} {} {} {}'.format(tonim.getNome(),tonim.getVelocidadem(),tonim.getVida(),tonim.getX(),tonim.getY()))
#15
colide(zak,galou)
#16
colide(zak,tonim)
#17
colide(tonim,galou)
#18
colide(zak,tonim)







