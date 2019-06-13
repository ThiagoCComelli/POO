# -*- coding: utf-8 -*-
dia1, mes1 = map(int,input().split())
dia2, mes2 = map(int,input().split())
if dia1 == dia2 and mes1 == mes2:
    print("0")
elif mes1 == mes2:
    dia = dia2-dia1
    print(dia)
elif mes2 > mes1:
    if dia2 < dia1:
        mes = (mes2-mes1)-1
        dia = (mes*30)+abs(dia2-dia1)
    print(dia)

