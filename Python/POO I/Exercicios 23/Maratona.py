# -*- coding: utf-8 -*-
class Pessoa():
    def __init__(self,nome):
        self.nome = nome

class Aluno(Pessoa):
    def __init__(self,nome,anoNas,anoIni,mundial,regional):
        super().__init__(nome)
        self.__anoNas = anoNas
        self.__anoIni = anoIni
        self.__mundial = mundial
        self.__regional = regional

    def __repr__(self):
        return 'Nome: %s, Nascimento: %s, Inicio: %s, Mundial: %s, Regional: %s'\
               %(self.nome,self.__anoNas,self.__anoIni,self.__mundial,self.__regional)

    def alunoElegivel(self):
        if self.__mundial > 1 or self.__regional > 4:
            return False
        elif self.__anoIni <= 2014 and self.__anoNas <= 1995:
            return False
        else:
            return True

class Coach(Pessoa):
    def __init__(self,nome):
        super().__init__(nome)

    def __repr__(self):
        return 'Coach: %s'%(self.nome)

class Time():
    def __init__(self,nometi,alunos,coach):
        self.__nometi = nometi
        self.__alunos = alunos
        self.__coach = coach

    def timeValido(self):
        valido = True
        if len(self.__alunos) == 3 and self.__coach != None:
            for i in self.__alunos:
                valido = i.alunoElegivel()
                if not valido:
                    break
            return valido
        else:
            return False

    def __repr__(self):
        return 'Time: %s, Alunos: %s, Coach: %s'\
        %(self.__nometi,self.__alunos,self.__coach)

a = Aluno('joao',2000,2018,1,1)
b = Aluno('toni',2000,2014,1,1)
c = Aluno('silva',2000,2013,1,1)
d = Coach('Maicon')
e = Time('DeveSerIsso',[a,b,c],d.nome)
print(a)
print('Elegivel: %s'%a.alunoElegivel())
print(b)
print('Elegivel: %s'%b.alunoElegivel())
print(c)
print('Elegivel: %s'%c.alunoElegivel())
print(e)
print('Elegivel: %s'%e.timeValido())
print()

f = Aluno('ola',2000,2018,6,1)
g = Aluno('bomdia',2000,2014,1,1)
h = Aluno('boanoite',2000,2013,1,1)
i = Coach('Cleiton')
j = Time('Outro',[f,g,h],i.nome)
print(f)
print('Elegivel: %s'%f.alunoElegivel())
print(g)
print('Elegivel: %s'%g.alunoElegivel())
print(h)
print('Elegivel: %s'%h.alunoElegivel())
print(j)
print('Elegivel: %s'%j.timeValido())
print()

k = Aluno('joao',2000,2018,1,1)
l = Aluno('toni',2000,2014,1,1)
m = Coach('Maicon')
n = Time('DeveSerIsso',[k,l],m.nome)
print(k)
print('Elegivel: %s'%k.alunoElegivel())
print(l)
print('Elegivel: %s'%l.alunoElegivel())
print(n)
print('Elegivel: %s'%n.timeValido())