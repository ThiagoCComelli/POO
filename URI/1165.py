# -*- coding: utf-8 -*-
n = int(input())
for i in range(n):
    primo = True
    v = int(input())
    for l in range(2,v):
        if (v%l)==0:
            primo = False
            break
    if (primo) == True:
        print(v,"eh primo")
    else:
        print(v,"nao eh primo")

