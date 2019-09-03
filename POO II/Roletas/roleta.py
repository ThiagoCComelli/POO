import tkinter as tk
import time
import tkinter
from tkinter import *
from random import randint,shuffle
import random

class Roleta():
    def __init__(self):
        self.__roletaeuro = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36]
        self.__roletafran = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36]
        self.__roletaame = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36]

    def getNumEuro(self):
        num = random.choice(self.__roletaeuro)
        return num

    def getNumFran(self):
        num = random.choice(self.__roletafran)
        return num

    def getNumAme(self):
        num = random.choice(self.__roletaame)
        return num


