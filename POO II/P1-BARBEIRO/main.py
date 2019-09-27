# Import nas bibliotecas Tkinter, importei tudo por que durante o projeto da roleta, tive alguns problemas onde nao reconhecia certas funcoes do Tkinter
import tkinter as tk
import tkinter
from tkinter import *
# from tkinter.ttk import *

# Import nas classes que estao em outros arquivos
from cliente import Cliente

class Estabelecimento():
    def __init__(self,master):
        self.__nome = "sei la"
        self.root = root.geometry("800x600"), root.resizable(width=False, height=False)
        self.__cliente = Cliente()
        # self.__estoque = Estoque()
        self.telalogin()

    # Verifica se o usuario é valido, por padrao todas as respostas é admin
    def verificaLogin(self,nome,senha,secreto):
        if nome == "admin" and senha == "admin" and secreto == "admin":
            self.frame1.place_forget()
            self.telaDaComercio()
        else:
            print("invalido")

    def getCliente(self):
        return self.__cliente

    # tela de login intereacao com usuario
    def telalogin(self):
        # frame1 é a tela de login
        nomes = StringVar()
        senhas = StringVar()
        secretos = StringVar()

        self.frame1 = tk.Frame(root, width = 800, height = 600,bg = 'black')
        self.frame1.place(x=0,y=0)

        self.login = tk.Label(self.frame1)
        self.login.configure(text='TELA DE LOGIN DA BARBEARIA',font="Times 25 bold", fg="WHITE", bg="black")
        self.login.place(x=60, y=30)

        self.nometexto = tk.Label(self.frame1)
        self.nometexto.configure(text='NOME:', font="Times 15 bold", fg="WHITE",bg="BLACK")
        self.nometexto.place(x=50, y=170)
        self.nome = Entry(self.frame1, textvariable=nomes).place(x=50, y=200)

        self.senhatexto = tk.Label(self.frame1)
        self.senhatexto.configure(text='SENHA:', font="Times 15 bold", fg="WHITE",bg="BLACK")
        self.senhatexto.place(x=50, y=250)
        self.senha = Entry(self.frame1, textvariable=senhas, show="*").place(x=50, y=280)

        self.secretotexto = tk.Label(self.frame1)
        self.secretotexto.configure(text='RESPOTAS SECRETA: (LOGIN PADRAO PARA TODO SISTEMA)', font="Times 15 bold", fg="WHITE", bg="BLACK")
        self.secretotexto.place(x=50, y=330)
        self.secreto = Entry(self.frame1, textvariable=secretos, show="*").place(x=50, y=360)

        self.cola = tk.Label(self.frame1)
        self.cola.configure(text='login/senha/resposta: admin/admin/admin', font="Times 15 bold",fg="gray", bg="BLACK")
        self.cola.place(x=10, y=570)

        self.botaoVerifica = tkinter.Button(self.frame1, text="VERIFICA", width=13, command=lambda: self.verificaLogin(nomes.get(),senhas.get(),secretos.get()), fg="black", font="Times 13 bold").place(x=50, y=440)

    # Interacao com usuario add e remove item da cesta
    def telaDaComercio(self):
        # frame2 é a tela do comercio
        # frame3 é a tela da esquerda
        # frame4 é a tela da direita
        # frame5 é a tela do meio

        self.frame2 = tk.Frame(root, width=800, height=600, bg='gray')
        self.frame2.place(x=0, y=0)

        self.frame3 = tk.Frame(root, width=250, height=400, bg='white')
        self.frame3.place(x=50,y=150)

        self.frame4 = tk.Frame(root, width=250, height=400, bg='white')
        self.frame4.place(x=500, y=150)

        self.frame5 = tk.Frame(root, width=160, height=400, bg='white')
        self.frame5.place(x=320, y=150)

        self.nomedaloja = tk.Label(self.frame2)
        self.nomedaloja.configure(text='BARBEARIA DA UFSC', font="Times 45 bold underline italic", fg="black", bg="gray")
        self.nomedaloja.place(x=60, y=30)

        self.ingredientes = tk.Label(self.frame2)
        self.ingredientes.configure(text='PRODUTOS E SEVICOS', font="Times 15 bold", fg="black",bg="gray")
        self.ingredientes.place(x=50, y=120)

        self.seulanche = tk.Label(self.frame2)
        self.seulanche.configure(text='SUA CESTA', font="Times 15 bold", fg="black", bg="gray")
        self.seulanche.place(x=560, y=120)

        self.obs = tk.Label(self.frame2)
        self.obs.configure(text='*Os produtos (CORTE ESTILOSO e BARBA ESTILOSA), são limitados à apenas uma por usuario', font="Times 14 bold", fg="light gray", bg="gray")
        self.obs.place(x=10, y=570)

        self.produtosFrame()
        self.cestaFrame()
        self.telaMeio()

        self.update()

    # update nas variaveis da tela do meio, atualiza a interface da sua cesta de produtos
    def update(self):
        a = self.__cliente.getCesta()

        self.pao1.configure(text='{}'.format(a.count("cabelo")), font="Times 15 bold", fg="black", bg="white")
        self.ham1.configure(text='{}'.format(a.count("barba")), font="Times 15 bold", fg="black", bg="white")
        self.tot1.configure(text='{}'.format(a.count("cremebarba")), font="Times 15 bold", fg="black", bg="white")
        self.que1.configure(text='{}'.format(a.count("cremepele")), font="Times 15 bold", fg="black", bg="white")
        self.bat1.configure(text='{}'.format(a.count("xampu")), font="Times 15 bold", fg="black", bg="white")
        self.bac1.configure(text='{}'.format(a.count("desodorante")), font="Times 15 bold", fg="black", bg="white")
        self.cor1.configure(text='{}'.format(a.count("acessorios")), font="Times 15 bold", fg="black", bg="white")

    # adiciona na cesta
    def adicionar(self,produto):
        self.__cliente.addNaCesta(produto)
        self.update()

    # removve da cesta
    def remover(self,produto):
        self.__cliente.remDaCesta(produto)
        self.update()

    # nota fiscal, tela final
    def checkout(self):
        a = self.__cliente.getCesta()

        if len(a) > 0:
            self.frame2.place_forget()
            self.frame3.place_forget()
            self.frame4.place_forget()
            self.frame5.place_forget()

            self.frame6 = tk.Frame(root, width=800, height=600, bg='gray')
            self.frame6.place(x=0, y=0)

            self.telafinal = tk.Label(self.frame6)
            self.telafinal.configure(text='CHECKOUT:', font="Times 45 bold underline italic", fg="black", bg="gray")
            self.telafinal.place(x=70, y=10)

            self.valores = tk.Label(self.frame6)
            self.valores.configure(text='', font="Times 45 bold", fg="black", bg="gray")
            self.valores.place(x=70, y=10)

            self.total = tk.Label(self.frame6)
            self.total.configure(text='TOTAL: {} $'.format(self.__cliente.getPagar()), font="Times 45 bold", fg="black", bg="gray")
            self.total.place(x=400, y=500)

            b = set(a)
            cod = []
            for i in b:
                cod.append(i)

            x = 450
            y = 25
            for i in range(len(b)):
                var = ""
                var += "{}-x-{}".format(cod[i],a.count(cod[i]))
                self.valores = tk.Label(self.frame6)
                self.valores.configure(text='{}'.format(var), font="Times 30 bold", fg="black", bg="gray")
                self.valores.place(x=x, y=y)
                y += 50

    # cesta de produtos do usuario (parte visual)
    def telaMeio(self):

        self.pao1 = tk.Label(self.frame5)
        self.pao1.configure(text='{}', font="Times 15 bold", fg="black", bg="white")
        self.pao1.place(x=70, y=10)

        self.ham1 = tk.Label(self.frame5)
        self.ham1.configure(text='{}', font="Times 15 bold", fg="black", bg="white")
        self.ham1.place(x=70, y=50)

        self.tot1 = tk.Label(self.frame5)
        self.tot1.configure(text='{}', font="Times 15 bold", fg="black", bg="white")
        self.tot1.place(x=70, y=90)

        self.que1 = tk.Label(self.frame5)
        self.que1.configure(text='{}', font="Times 15 bold", fg="black", bg="white")
        self.que1.place(x=70, y=130)

        self.bat1 = tk.Label(self.frame5)
        self.bat1.configure(text='{}', font="Times 15 bold", fg="black", bg="white")
        self.bat1.place(x=70, y=170)

        self.bac1 = tk.Label(self.frame5)
        self.bac1.configure(text='{}', font="Times 15 bold", fg="black", bg="white")
        self.bac1.place(x=70, y=210)

        self.cor1 = tk.Label(self.frame5)
        self.cor1.configure(text='{}', font="Times 15 bold", fg="black", bg="white")
        self.cor1.place(x=70, y=250)

        comprar = tk.Button(self.frame5, text="COMPRAR", width=10, fg="black",bg="light gray",command= lambda:self.checkout(), font="Times 13 bold").place(x=20, y=350)

    # usuario escolhe o produto
    def produtosFrame(self):

        self.pao1 = tk.Label(self.frame3)
        self.pao1.configure(text='CORTE ESTILOSO $25',font="Times 15 bold", fg="black", bg="white")
        self.pao1.place(x=10, y=10)

        self.pao1 = tk.Label(self.frame3)
        self.pao1.configure(text='BARBA ESTILOSA $20',font="Times 15 bold", fg="black", bg="white")
        self.pao1.place(x=10, y=50)

        self.pao1 = tk.Label(self.frame3)
        self.pao1.configure(text='CREME P/ BARBA $10',font="Times 15 bold", fg="black", bg="white")
        self.pao1.place(x=10, y=90)

        self.pao1 = tk.Label(self.frame3)
        self.pao1.configure(text='CREME P/ O ROSTO $15',font="Times 15 bold", fg="black", bg="white")
        self.pao1.place(x=10, y=130)

        self.pao1 = tk.Label(self.frame3)
        self.pao1.configure(text='XAMPU $8',font="Times 15 bold", fg="black", bg="white")
        self.pao1.place(x=10, y=170)

        self.pao1 = tk.Label(self.frame3)
        self.pao1.configure(text='DESODORANTE $11',font="Times 15 bold", fg="black", bg="white")
        self.pao1.place(x=10, y=210)

        self.pao1 = tk.Label(self.frame3)
        self.pao1.configure(text='ACESSORIOS $14',font="Times 15 bold", fg="black", bg="white")
        self.pao1.place(x=10, y=250)

        paob = tkinter.Button(self.frame2, text="+", width=1, fg="black",bg="green",command= lambda: self.adicionar("cabelo"), font="Times 13 bold").place(x=7, y=155)
        hamb = tkinter.Button(self.frame2, text="+", width=1, fg="black",bg="green",command= lambda: self.adicionar("barba"), font="Times 13 bold").place(x=7, y=195)
        tomb = tkinter.Button(self.frame2, text="+", width=1, fg="black",bg="green",command= lambda: self.adicionar("cremebarba"), font="Times 13 bold").place(x=7, y=235)
        queb = tkinter.Button(self.frame2, text="+", width=1, fg="black",bg="green",command= lambda: self.adicionar("cremepele"), font="Times 13 bold").place(x=7, y=275)
        batb = tkinter.Button(self.frame2, text="+", width=1, fg="black",bg="green",command= lambda: self.adicionar("xampu"), font="Times 13 bold").place(x=7, y=315)
        vacb = tkinter.Button(self.frame2, text="+", width=1, fg="black",bg="green",command= lambda: self.adicionar("desodorante"), font="Times 13 bold").place(x=7, y=355)
        corb = tkinter.Button(self.frame2, text="+", width=1, fg="black",bg="green",command= lambda: self.adicionar("acessorios"), font="Times 13 bold").place(x=7, y=395)

    # remove da sua cesta um produto que voce nao quer mais
    def cestaFrame(self):
        self.pao2 = tk.Label(self.frame4)
        self.pao2.configure(text='CORTE ESTILOSO $25', font="Times 15 bold", fg="black", bg="white")
        self.pao2.place(x=10, y=10)

        self.pao2 = tk.Label(self.frame4)
        self.pao2.configure(text='BARBA ESTILOSA $20', font="Times 15 bold", fg="black", bg="white")
        self.pao2.place(x=10, y=50)

        self.pao2 = tk.Label(self.frame4)
        self.pao2.configure(text='CREME P/ BARBA $10', font="Times 15 bold", fg="black", bg="white")
        self.pao2.place(x=10, y=90)

        self.pao2 = tk.Label(self.frame4)
        self.pao2.configure(text='CREME P/ O ROSTO $15', font="Times 15 bold", fg="black", bg="white")
        self.pao2.place(x=10, y=130)

        self.pao2 = tk.Label(self.frame4)
        self.pao2.configure(text='XAMPU $8', font="Times 15 bold", fg="black", bg="white")
        self.pao2.place(x=10, y=170)

        self.pao2 = tk.Label(self.frame4)
        self.pao2.configure(text='DESODORANTE $11', font="Times 15 bold", fg="black", bg="white")
        self.pao2.place(x=10, y=210)

        self.pao2 = tk.Label(self.frame4)
        self.pao2.configure(text='ACESSORIOS $14', font="Times 15 bold", fg="black", bg="white")
        self.pao2.place(x=10, y=250)

        paobb = tkinter.Button(self.frame2, text="-", width=1, fg="black", bg="red",command= lambda: self.remover("cabelo"), font="Times 13 bold").place(x=755,y=155)
        hambb = tkinter.Button(self.frame2, text="-", width=1, fg="black", bg="red",command= lambda: self.remover("barba"), font="Times 13 bold").place(x=755,y=195)
        tombb = tkinter.Button(self.frame2, text="-", width=1, fg="black", bg="red",command= lambda: self.remover("cremebarba"), font="Times 13 bold").place(x=755,y=235)
        quebb = tkinter.Button(self.frame2, text="-", width=1, fg="black", bg="red",command= lambda: self.remover("cremepele"), font="Times 13 bold").place(x=755,y=275)
        batbb = tkinter.Button(self.frame2, text="-", width=1, fg="black", bg="red",command= lambda: self.remover("xampu"), font="Times 13 bold").place(x=755,y=315)
        vacbb = tkinter.Button(self.frame2, text="-", width=1, fg="black", bg="red",command= lambda: self.remover("desodorante"), font="Times 13 bold").place(x=755,y=355)
        corbb = tkinter.Button(self.frame2, text="-", width=1, fg="black", bg="red",command= lambda: self.remover("acessorios"), font="Times 13 bold").place(x=755,y=395)


root = tk.Tk()
Estabelecimento(root)
root.mainloop()