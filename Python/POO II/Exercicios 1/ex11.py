# -*- coding: utf-8 -*-
a,b,c = map(float,input().split())
grade = (a+b+c)/3
if grade < 3:
    print("Reprovado")
elif 3 >= grade and grade <= 5.75:
    print("Exame")
elif grade >= 5.76:
    print("Aprovado")