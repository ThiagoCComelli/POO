import tkinter as tk
import time
import tkinter
from tkinter import *
from random import randint
from roleta import Roleta
from players import Player

class A:
    def __init__(self, master):
        self.menu()
        self.roleta = Roleta()

    def menu(self):
        self.photo = PhotoImage(file="preto.gif")
        self.backlabel = Label(root, image=self.photo).place(x=-1, y=-1)

        self.titulo = tk.Label(root)
        self.titulo.grid(row=0, column=0)
        self.titulo.configure(text='JOGO DA ROLETA!', font="Times 25 bold",fg="red",bg="black")
        self.titulo.place(x=250,y=50)
        self.root = root.geometry("1850x1013"), root.resizable(width=False, height=False)
        self.buttonsMenu()

    def voltarMenu(self):
        self.menu()
        self.buttonsMenu()

    def apostas(self):
        ap3 = tkinter.Button(master=root,text="",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold").place(x=568,y=462)
        ap6 = tkinter.Button(master=root,text="",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold").place(x=663,y=462)
        ap9 = tkinter.Button(master=root,text="",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold").place(x=757,y=462)
        ap12 = tkinter.Button(master=root,text="",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold").place(x=855,y=462)
        ap15 = tkinter.Button(master=root,text="",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold").place(x=950,y=462)
        ap18 = tkinter.Button(master=root,text="",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold").place(x=1051,y=462)
        ap21 = tkinter.Button(master=root,text="",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold").place(x=1145,y=462)
        ap24 = tkinter.Button(master=root,text="",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold").place(x=1242,y=462)
        ap27 = tkinter.Button(master=root,text="",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold").place(x=1340,y=462)
        ap30 = tkinter.Button(master=root,text="",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold").place(x=1436,y=462)
        ap33 = tkinter.Button(master=root,text="",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold").place(x=1533,y=462)
        ap36 = tkinter.Button(master=root,text="",width=1,height=0,fg="red",bg="yellow",font="Times 13 bold").place(x=1630,y=462)

        ap2 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=568, y=615)
        ap5 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=663, y=615)
        ap8 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=757, y=615)
        ap11 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=855, y=615)
        ap14 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=950, y=615)
        ap17 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=1051, y=615)
        ap20 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=1145, y=615)
        ap23 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=1242, y=615)
        ap26 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=1340, y=615)
        ap29 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=1436, y=615)
        ap32 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=1533, y=615)
        ap35 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=1630, y=615)

        ap1 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=568, y=769)
        ap4 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=663, y=769)
        ap7 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=757, y=769)
        ap10 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=855, y=769)
        ap13 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=950, y=769)
        ap16 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=1051, y=769)
        ap19 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=1145, y=769)
        ap22 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=1242, y=769)
        ap25 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=1340, y=769)
        ap28 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=1436, y=769)
        ap31 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=1533, y=769)
        ap34 = tkinter.Button(master=root, text="", width=1, height=0, fg="red", bg="yellow",font="Times 13 bold").place(x=1630, y=769)




    def buttonsMenu(self):
        add1 = tkinter.Button(master=root,text="EUROPEU",width=13,command=self.europeu,fg="red",bg="black",font="Times 13 bold").place(x=100,y=100)
        add2 = tkinter.Button(master=root,text="AMERICANO",width=13,command=self.americano,fg="red",bg="black",font=("Times 13 bold")).place(x=100,y=135)
        add3 = tkinter.Button(master=root, text="FRANCES", width=13, command=self.frances,fg="red",bg="black",font=("Times 13 bold")).place(x=100, y=170)

    def europeu(self):
        self.photo = PhotoImage(file="tabela.gif")
        self.backlabel = Label(root, image=self.photo).place(x=-1,y=-1)

        self.titulo = tk.Label()
        self.titulo.grid(row=0, column=0)
        self.titulo.configure(text='EUROPEU', font="Times 25 bold",fg="red",bg="black")
        self.titulo.place(x=325)

        voltar = tkinter.Button(master=root,text="voltar para o menu",width=15,command=self.voltarMenu,fg="red",bg="black",font=("Times 13 bold")).place(x=10,y=10)

        self.apostas()

    def americano(self):
        self.photo = PhotoImage(file="tabela.gif")
        self.backlabel = Label(root, image=self.photo).place(x=-1,y=-1)

        self.titulo = tk.Label()
        self.titulo.grid(row=0, column=0)
        self.titulo.configure(text='AMERICANO', font="Times 25 bold",fg="red",bg="black")
        self.titulo.place(x=325)

        voltar = tkinter.Button(master=root,text="voltar para o menu",width=15,command=self.voltarMenu,fg="red",bg="black",font=("Times 13 bold")).place(x=93,y=745)

        self.apostas()

    def frances(self):
        self.photo = PhotoImage(file="tabela.gif")
        self.backlabel = Label(root, image=self.photo).place(x=-1,y=-1)

        self.titulo = tk.Label()
        self.titulo.grid(row=0, column=0)
        self.titulo.configure(text='FRANCES', font="Times 25 bold",fg="red",bg="black")
        self.titulo.place(x=325)

        voltar = tkinter.Button(master=root,text="voltar para o menu",width=15,command=self.voltarMenu,fg="red",bg="black",font=("Times 13 bold")).place(x=93,y=745)

        self.apostas()




root = tk.Tk()
A(root)
root.mainloop()
