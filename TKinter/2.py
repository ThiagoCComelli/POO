import tkinter as tk
import time
import tkinter
from tkinter import *

class A:
    def __init__(self, master):
        self.titulo=tk.Label(master)
        self.titulo.grid(row=0, column=0)
        self.titulo.configure(text='Somador!',font=("Arial",25))
        self.titulo.place(x=325)
        self.root = root.geometry("800x800"),root.resizable(width=False,height=False)
        self.sum = 0
        self.cout()
        self.buttons()

    def cout(self):
        try:
            self.cout = tk.Label(root)
            self.cout.grid()
            self.cout.configure(text=self.sum,font=("Arial",25))
            self.cout.place(x=400,y=50)
        except Exception:
            return False

    def um(self):
        self.sum += 1
        self.cout.configure(text=self.sum)
        self.cout

    def dois(self):
        self.sum += 2
        self.cout.configure(text=self.sum)
        self.cout

    def cinco(self):
        self.sum += 5
        self.cout.configure(text=self.sum)
        self.cout

    def dez(self):
        self.sum += 10
        self.cout.configure(text=self.sum)
        self.cout

    def vinte(self):
        self.sum += 20
        self.cout.configure(text=self.sum)
        self.cout

    def cinquenta(self):
        self.sum += 50
        self.cout.configure(text=self.sum)
        self.cout

    def cem(self):
        self.sum += 100
        self.cout.configure(text=self.sum)
        self.cout

    def buttons(self):
        add1 = tkinter.Button(master=root,text="Adiciona 1",width=13,command=self.um).place(x=100,y=100)
        add2 = tkinter.Button(master=root,text="Adiciona 2",width=13,command=self.dois).place(x=100,y=135)
        add5 = tkinter.Button(master=root,text="Adiciona 5",width=13,command=self.cinco).place(x=100,y=170)
        add10 = tkinter.Button(master=root,text="Adiciona 10",width=13,command=self.dez).place(x=100,y=205)
        add20 = tkinter.Button(master=root,text="Adiciona 20",width=13,command=self.vinte).place(x=100,y=240)
        add50 = tkinter.Button(master=root,text="Adiciona 50",width=13,command=self.cinquenta).place(x=100,y=275)
        add100 = tkinter.Button(master=root,text="Adiciona 100",width=13,command=self.cem).place(x=100,y=310)

root = tk.Tk()
A(root)
root.mainloop()