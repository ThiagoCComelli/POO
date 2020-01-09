# -*- coding: utf-8 -*-
for i in range(1):
    primo = True
    v = int(input())
    for l in range(2,v):
        if (v%l)==0:
            primo = False
            break
    if (primo) == True:
        print(v,"e primo")
    else:
        print(v,"nao e primo")