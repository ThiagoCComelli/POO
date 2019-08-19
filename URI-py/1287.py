# -*- coding: utf-8 -*-
while True:
    try:
        co = False
        lista = [input()]
        lista1 = []
        nome = ""
        for i in lista:
            for u in i:
                if u != ' ' and u != ',':
                    lista1.append(u)

        for i in lista1:
            if i != 'o' and i != 'O' and i != 'l' and not i.isdigit():
                co = True
            elif i == 'o' or i == 'O':
                nome += "0"
            elif i == 'l':
                nome += "1"
            elif i.isdigit():
                nome += i
        if len(nome) == 0:
            print("error")
        else:
            if int(nome) > 2147483647:
                print('error')
            elif co == False:
                nome = int(nome)
                print(nome)
            else:
                print('error')
    except EOFError:
        break