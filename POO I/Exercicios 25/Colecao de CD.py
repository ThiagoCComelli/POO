# -*- coding: utf-8 -*-
class Cd():
    def __init__(self,capacidade = 0,titulo='',id=0,nome='',membros=[],musicas=[]):
        self.__capacidade = capacidade
        self.__titulo = titulo
        self.__nome = nome
        self.__membros = membros
        self.__id = id
        self.__musicas = musicas


class Musica():
    def __init__(self,nome,duracao,tamanho):
        self.__nome = nome
        self.__duracao = duracao
        self.__tamanho = tamanho


class Pessoa():
    def __init__(self,nome):
        self.__nome = nome