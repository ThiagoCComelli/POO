import tkinter as tk
import time
import tkinter
from tkinter import *
from random import randint
from roleta import Roleta
from players import Player


class A:
    def __init__(self, master):
        self.roleta = Roleta()
        self.players = 0
        self.playersjogando = []
        self.modo = "NENHUM"
        self.banco = 1000
        self.apostados = []
        self.menu()

    def menu(self):
        self.photo = PhotoImage(file="preto.gif")
        self.backlabel = Label(root, image=self.photo).place(x=-1, y=-1)

        self.titulo = tk.Label(root)
        self.titulo.grid(row=0, column=0)
        self.titulo.configure(text='JOGO DA ROLETA!', font="Times 25 bold", fg="red", bg="black")
        self.titulo.place(x=750, y=50)

        self.jogadorestit = tk.Label(root)
        self.jogadorestit.grid(row=0, column=0)
        self.jogadorestit.configure(text='QUANTIDADE DE JOGADORES: {}'.format(self.players), font="Times 25 bold",
                                    fg="red", bg="black")
        self.jogadorestit.place(x=1000, y=450)

        self.modedejogotit = tk.Label(root)
        self.modedejogotit.grid(row=0, column=0)
        self.modedejogotit.configure(text='MODO DE JOGO: {}'.format(self.modo), font="Times 25 bold", fg="red",
                                     bg="black")
        self.modedejogotit.place(x=1000, y=300)

        self.modedejogo = tk.Label(root)
        self.modedejogo.grid(row=0, column=0)
        self.modedejogo.configure(text='MODO DE JOGO:', font="Times 25 bold", fg="red", bg="black")
        self.modedejogo.place(x=100, y=300)

        self.jogadores = tk.Label(root)
        self.jogadores.grid(row=0, column=0)
        self.jogadores.configure(text='JOADORES:', font="Times 25 bold", fg="red", bg="black")
        self.jogadores.place(x=181, y=450)

        self.root = root.geometry("1850x1013"), root.resizable(width=False, height=False)

        add1 = tkinter.Button(master=root, text="EUROPEU", width=13, command=lambda: self.setModo("EUROPEU"), fg="red",
                              bg="black", font="Times 13 bold").place(x=400, y=300)
        add2 = tkinter.Button(master=root, text="AMERICANO", width=13, command=lambda: self.setModo("AMERICANO"),
                              fg="red", bg="black", font=("Times 13 bold")).place(x=400, y=335)
        add3 = tkinter.Button(master=root, text="FRANCES", width=13, command=lambda: self.setModo("FRANCES"), fg="red",
                              bg="black", font=("Times 13 bold")).place(x=400, y=370)

        add4 = tkinter.Button(master=root, text="UM JOGADOR", width=20, command=lambda: self.setpl(1), fg="red",
                              bg="black", font=("Times 13 bold")).place(x=400, y=450)
        add5 = tkinter.Button(master=root, text="DOIS JOGADORES", width=20, command=lambda: self.setpl(2), fg="red",
                              bg="black", font=("Times 13 bold")).place(x=400, y=485)
        add6 = tkinter.Button(master=root, text="TRES JOGADORES", width=20, command=lambda: self.setpl(3), fg="red",
                              bg="black", font=("Times 13 bold")).place(x=400, y=520)
        add7 = tkinter.Button(master=root, text="QUATRO JOGADORES", width=20, command=lambda: self.setpl(4), fg="red",
                              bg="black", font=("Times 13 bold")).place(x=400, y=555)

        add8 = tkinter.Button(master=root, text="JOGAR", width=20, command=self.jogar, fg="red", bg="black",
                              font=("Times 13 bold")).place(x=1000, y=600)

    def apostas(self):

        ap3 = tkinter.Button(master=root, text="3", width=1, height=0, fg="red", bg="yellow",
                             font="Times 13 bold").place(x=568, y=462)
        ap6 = tkinter.Button(master=root, text="6", width=1, height=0, fg="red", bg="yellow",
                             font="Times 13 bold").place(x=663, y=462)
        ap9 = tkinter.Button(master=root, text="9", width=1, height=0, fg="red", bg="yellow",
                             font="Times 13 bold").place(x=757, y=462)
        ap12 = tkinter.Button(master=root, text="12", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=855, y=462)
        ap15 = tkinter.Button(master=root, text="15", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=950, y=462)
        ap18 = tkinter.Button(master=root, text="18", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1051, y=462)
        ap21 = tkinter.Button(master=root, text="21", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1145, y=462)
        ap24 = tkinter.Button(master=root, text="24", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1242, y=462)
        ap27 = tkinter.Button(master=root, text="27", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1340, y=462)
        ap30 = tkinter.Button(master=root, text="30", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1436, y=462)
        ap33 = tkinter.Button(master=root, text="33", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1533, y=462)
        ap36 = tkinter.Button(master=root, text="36", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1630, y=462)

        ap2 = tkinter.Button(master=root, text="2", width=1, height=0, fg="red", bg="yellow",
                             font="Times 13 bold").place(x=568, y=615)
        ap5 = tkinter.Button(master=root, text="5", width=1, height=0, fg="red", bg="yellow",
                             font="Times 13 bold").place(x=663, y=615)
        ap8 = tkinter.Button(master=root, text="8", width=1, height=0, fg="red", bg="yellow",
                             font="Times 13 bold").place(x=757, y=615)
        ap11 = tkinter.Button(master=root, text="11", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=855, y=615)
        ap14 = tkinter.Button(master=root, text="14", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=950, y=615)
        ap17 = tkinter.Button(master=root, text="17", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1051, y=615)
        ap20 = tkinter.Button(master=root, text="20", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1145, y=615)
        ap23 = tkinter.Button(master=root, text="23", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1242, y=615)
        ap26 = tkinter.Button(master=root, text="25", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1340, y=615)
        ap29 = tkinter.Button(master=root, text="29", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1436, y=615)
        ap32 = tkinter.Button(master=root, text="32", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1533, y=615)
        ap35 = tkinter.Button(master=root, text="35", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1630, y=615)

        ap1 = tkinter.Button(master=root, text="1", width=1, height=0, fg="red", bg="yellow",
                             font="Times 13 bold").place(x=568, y=769)
        ap4 = tkinter.Button(master=root, text="4", width=1, height=0, fg="red", bg="yellow",
                             font="Times 13 bold").place(x=663, y=769)
        ap7 = tkinter.Button(master=root, text="7", width=1, height=0, fg="red", bg="yellow",
                             font="Times 13 bold").place(x=757, y=769)
        ap10 = tkinter.Button(master=root, text="10", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=855, y=769)
        ap13 = tkinter.Button(master=root, text="13", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=950, y=769)
        ap16 = tkinter.Button(master=root, text="16", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1051, y=769)
        ap19 = tkinter.Button(master=root, text="19", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1145, y=769)
        ap22 = tkinter.Button(master=root, text="22", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1242, y=769)
        ap25 = tkinter.Button(master=root, text="25", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1340, y=769)
        ap28 = tkinter.Button(master=root, text="28", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1436, y=769)
        ap31 = tkinter.Button(master=root, text="31", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1533, y=769)
        ap34 = tkinter.Button(master=root, text="34", width=1, height=0, fg="red", bg="yellow",
                              font="Times 13 bold").place(x=1630, y=769)

        um = tkinter.Button(master=root, text="1", width=5, height=0, fg="red", bg="black", font="Times 13 bold").place(
            x=50, y=750)
        dois = tkinter.Button(master=root, text="2", width=5, height=0, fg="red", bg="black",
                              font="Times 13 bold").place(x=130, y=750)
        tres = tkinter.Button(master=root, text="3", width=5, height=0, fg="red", bg="black",
                              font="Times 13 bold").place(x=210, y=750)
        quatro = tkinter.Button(master=root, text="4", width=5, height=0, fg="red", bg="black",
                                font="Times 13 bold").place(x=50, y=790)
        cinco = tkinter.Button(master=root, text="5", width=5, height=0, fg="red", bg="black",
                               font="Times 13 bold").place(x=130, y=790)
        seis = tkinter.Button(master=root, text="6", width=5, height=0, fg="red", bg="black",
                              font="Times 13 bold").place(x=210, y=790)
        sete = tkinter.Button(master=root, text="7", width=5, height=0, fg="red", bg="black",
                              font="Times 13 bold").place(x=50, y=830)
        oito = tkinter.Button(master=root, text="8", width=5, height=0, fg="red", bg="black",
                              font="Times 13 bold").place(x=130, y=830)
        nove = tkinter.Button(master=root, text="9", width=5, height=0, fg="red", bg="black",
                              font="Times 13 bold").place(x=210, y=830)
        zerar = tkinter.Button(master=root, text="ZERAR", width=5, height=0, fg="red", bg="black",
                               font="Times 13 bold").place(x=130, y=870)

        self.playeraposta = tk.Label()
        self.playeraposta.grid(row=0, column=0)
        self.playeraposta.place(x=100, y=100)

    def voltarMenu(self):
        if self.getPl() == 0:
            self.menu()
            self.buttonsMenu()

    def jogar(self):
        if self.getModo() == "AMERICANO":
            self.americano()
        elif self.getModo() == "EUROPEU":
            self.europeu()
        elif self.getModo() == "FRANCES":
            self.frances()

    def setpl(self, qtde):
        self.players = qtde
        self.jogadorestit.configure(text='QUANTIDADE DE JOGADORES: {}'.format(self.players), font="Times 25 bold",
                                    fg="red", bg="black")

    def setModo(self, modo):
        self.modo = modo
        self.modedejogotit.configure(text='MODO DE JOGO: {}'.format(self.modo), font="Times 25 bold", fg="red",
                                     bg="black")

    def getModo(self):
        return self.modo

    def getPl(self):
        return self.players

    def setPlayers(self):
        nome = ["ALPHA", "BETA", "CHARLIE", "DELTA"]
        for i in range(self.players):
            nome[i] = Player(nome[i])
            self.playersjogando.append(nome[i])

    def europeu(self):
        self.setPlayers()
        if self.getPl() != 0:
            self.photo = PhotoImage(file="tabela.gif")
            self.backlabel = Label(root, image=self.photo).place(x=-1, y=-1)

            self.titulo = tk.Label()
            self.titulo.grid(row=0, column=0)
            self.titulo.configure(text='EUROPEU', font="Times 25 bold", fg="red", bg="black")
            self.titulo.place(x=850)

            voltar = tkinter.Button(master=root, text="voltar para o menu", width=15, command=self.voltarMenu, fg="red",
                                    bg="black", font=("Times 13 bold")).place(x=10, y=10)

            self.apostas()

    def americano(self):
        self.setPlayers()
        if self.getPl() != 0:
            self.photo = PhotoImage(file="tabela.gif")
            self.backlabel = Label(root, image=self.photo).place(x=-1, y=-1)

            self.titulo = tk.Label()
            self.titulo.grid(row=0, column=0)
            self.titulo.configure(text='AMERICANO', font="Times 25 bold", fg="red", bg="black")
            self.titulo.place(x=850)

            voltar = tkinter.Button(master=root, text="voltar para o menu", width=15, command=self.voltarMenu, fg="red",
                                    bg="black", font=("Times 13 bold")).place(x=10, y=10)

            self.apostas()

    def frances(self):
        self.setPlayers()
        if self.getPl() != 0:
            self.photo = PhotoImage(file="tabela.gif")
            self.backlabel = Label(root, image=self.photo).place(x=-1, y=-1)

            self.titulo = tk.Label()
            self.titulo.grid(row=0, column=0)
            self.titulo.configure(text='FRANCES', font="Times 25 bold", fg="red", bg="black")
            self.titulo.place(x=850)

            voltar = tkinter.Button(master=root, text="voltar para o menu", width=15, command=self.voltarMenu, fg="red",
                                    bg="black", font=("Times 13 bold")).place(x=10, y=10)

            self.apostas()


root = tk.Tk()
A(root)
root.mainloop()


