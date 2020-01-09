# -*- coding: utf-8 -*-
import os
class JogoDaVelha():
    def __init__(self):
        self.__grade = [["_","_","_"],
                        ["_","_","_"],
                        ["_","_","_"]]
        self.__vez = 0
        self.__win = False

    def getVez(self):
        return self.__vez
    def getWin(self):
        return self.__win
    def setVez(self,x):
        self.__vez = x
    def setWin(self,x):
        self.__win = x

    def getGrade(self):
        grad = ""
        for i in self.__grade:
            for j in i:
                grad += j
                grad += "  "
            print(grad)
            grad = ""

    def getStatus(self):
        win = ""
        #linha
        if self.__grade[0][0] == self.__grade[0][1] and self.__grade[0][0] == self.__grade[0][2]:
            win = self.__grade[0][0]
        elif self.__grade[1][0] == self.__grade[1][1] and self.__grade[1][0] == self.__grade[1][2]:
            win = self.__grade[1][0]
        elif self.__grade[2][0] == self.__grade[2][1] and self.__grade[2][0] == self.__grade[2][2]:
            win = self.__grade[2][0]
        #coluna
        elif self.__grade[0][0] == self.__grade[1][0] and self.__grade[0][0] == self.__grade[2][0]:
            win = self.__grade[0][0]
        elif self.__grade[0][1] == self.__grade[1][1] and self.__grade[0][1] == self.__grade[2][1]:
            win = self.__grade[0][1]
        elif self.__grade[0][2] == self.__grade[1][2] and self.__grade[0][2] == self.__grade[2][2]:
            win = self.__grade[0][2]
        #diagonal
        elif self.__grade[0][0] == self.__grade[1][1] and self.__grade[0][0] == self.__grade[2][2]:
            win = self.__grade[0][0]
        elif self.__grade[0][2] == self.__grade[1][1] and self.__grade[0][2] == self.__grade[2][0]:
            win = self.__grade[0][2]

        if win == "x":
            print("Jogador '0' ganhou! (x)")
            self.getGrade()
            self.setWin(True)
        elif win == "o":
            print("Jogador '1' ganhou! (o)")
            self.getGrade()
            self.setWin(True)

    def jogar(self,linha,coluna):
        if self.getVez() == 0:
            col = 'x'
        elif self.getVez() == 1:
            col = 'o'
        while True:
            if self.__grade[linha-1][coluna-1] == "_":
                self.__grade[linha-1][coluna-1] = col
                break
            else:
                print("Jogada Invalida")
                linha,coluna = map(int,input("Faca sua jogada jogador {} (ex: 2 3)".format(self.getVez())).split())
                if linha <= 3 and linha >= 1 and coluna >= 1 and coluna <= 3:
                    pass
                else:
                    print("Jogada Invalida")
                    linha, coluna = map(int,input("Faca sua jogada jogador {} (ex: 2 3)".format(self.getVez())).split())

        if col == 'x':
            self.setVez(1)
        elif col == 'o':
            self.setVez(0)

        a.getStatus()

a = JogoDaVelha()
vez = "0"
while a.getWin() != True:
    os.system("clear")
    a.getGrade()
    linha,coluna = map(int,input("Faca sua jogada jogador {} (ex: 2 3)".format(vez[-1])).split())
    if linha <= 3 and linha >= 1 and coluna >= 1 and coluna <= 3:
        a.jogar(linha,coluna)
        if vez[-1] == "0":
            vez += "1"
        elif vez[-1] == "1":
            vez += "0"
    else:
        print("Jogada Invalida")