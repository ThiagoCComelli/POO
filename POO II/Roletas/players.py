import tkinter as tk
import time
import tkinter
from tkinter import *
from random import randint,shuffle
import random

class Player():
    def __init__(self,nome):
        self.__nome = nome
        self.__tips = 100

    def getNome(self):
        return self.__nome
    def getTip(self):
        return self.__tips

    def setTip(self,value):
        self.__tips += value