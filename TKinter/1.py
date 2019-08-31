# -*- coding: utf-8 -*-
import tkinter
from pygame import mixer
import random
import tkinter as tk
from tkinter import *


top = tkinter.Tk()
top.geometry("400x200")
top.resizable(width=False,height=False)
top.title("Mas uque é isso!")
texto = Label(top,text="Testando isso!")

def acao():
    print("Da que eu te dou outra")
    mixer.init(44100)
    d1 = mixer.Sound(random.choice(sons))
    d1.play()


birl = "birl.ogg"
bolso = "bolsok.ogg"
fdp = "FDP.ogg"
leroy = "leroy.ogg"

sons = [fdp]


button = tkinter.Button(master=top,text = 'Mas oque é isso',command = acao).place(x=100,y=100)

texto.pack()
top.mainloop()

"""
# -*- coding: utf-8 -*-
import tkinter
from pygame import mixer
import random
import tkinter as tk
from tkinter import *

top = tkinter.Tk()
top.geometry("800x800")
top.resizable(width=False,height=False)
top.title("Mas uque é isso!")
texto = Label(top,text="Somador!",font=("Arial",25))

tot = 0

result = Label(top,text=str(tot),font=("Arial",25))


def maisum():
    global tot
    tot += 1
    result.pack()

def maisdois():
    global tot
    tot += 2
    result.pack()

def maiscinco():
    global tot
    tot += 5
    result.pack()

def maisdez():
    global tot
    tot += 10
    result.pack()

def maisvinte():
    global tot
    tot += 20
    result.pack()

def maiscinquenta():
    global tot
    tot += 50
    result.pack()

def maiscem():
    global tot
    tot += 100
    result.pack()


button1 = tkinter.Button(master=top,text = 'Adiciona 1',command = maisum,width=13).place(x=100,y=100)
button2 = tkinter.Button(master=top,text = 'Adiciona 2',command = maisdois,width=13).place(x=100,y=150)
button5 = tkinter.Button(master=top,text = 'Adiciona 5',command = maiscinco,width=13).place(x=100,y=200)
button10 = tkinter.Button(master=top,text = 'Adiciona 10',command = maisdez,width=13).place(x=100,y=250)
button20 = tkinter.Button(master=top,text = 'Adiciona 20',command = maisvinte,width=13).place(x=100,y=300)
button50 = tkinter.Button(master=top,text = 'Adiciona 50',command = maiscinquenta,width=13).place(x=100,y=350)
button100 = tkinter.Button(master=top,text = 'Adiciona 100',command = maiscem,width=13).place(x=100,y=400)


texto.pack()
result.pack()
top.mainloop()


"""
