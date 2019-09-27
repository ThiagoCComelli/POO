# from produto import Estoque

class Cliente():
    def __init__(self):
        self.__cesta = []
        self.__pagar = 0

    def getCesta(self):
        return self.__cesta

    def getPagar(self):
        return self.__pagar

    # remove item da cesta
    def remDaCesta(self,item):
        if item in self.getCesta():
            if item == "cabelo":
                self.__cesta.remove(item)
                self.__pagar -= 25
            elif item == "barba":
                self.__cesta.remove(item)
                self.__pagar -= 20
            elif item == "cremebarba":
                self.__cesta.remove(item)
                self.__pagar -= 10
            elif item == "cremepele":
                self.__cesta.remove(item)
                self.__pagar -= 15
            elif item == "xampu":
                self.__cesta.remove(item)
                self.__pagar -= 8
            elif item == "desodorante":
                self.__cesta.remove(item)
                self.__pagar -= 11
            elif item == "acessorios":
                self.__cesta.remove(item)
                self.__pagar -= 14

    # adiciona item na cesta
    def addNaCesta(self,item):
        if item == "cabelo" and (item not in self.__cesta):
            self.__cesta.append(item)
            self.__pagar += 25
        elif item == "barba" and (item not in self.__cesta):
            self.__cesta.append(item)
            self.__pagar += 20
        elif item == "cremebarba":
            self.__cesta.append(item)
            self.__pagar += 10
        elif item == "cremepele":
            self.__cesta.append(item)
            self.__pagar += 15
        elif item == "xampu":
            self.__cesta.append(item)
            self.__pagar += 8
        elif item == "desodorante":
            self.__cesta.append(item)
            self.__pagar += 11
        elif item == "acessorios":
            self.__cesta.append(item)
            self.__pagar += 14

