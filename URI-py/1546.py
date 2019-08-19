# -*- coding: utf-8 -*-
n = int(input()) # dia de trabalho
for _ in range (0,n):
    k = int(input()) # numero de feedbacks
    for _ in range(0,k):
        c = int(input()) # categoria de 1 á 4
        if c == 1:
            print("Rolien")
        elif c == 2:
            print("Naej")
        elif c == 3:
            print("Elehcim")
        else:
            print("Odranoel")
