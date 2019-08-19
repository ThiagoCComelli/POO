# -*- coding: utf-8 -*-
while True:
    try:
        EPR = EHD = INTRUSOS = 0
        for i in range(int(input())):
            n,m = input().split()
            n = int(n)
            if m == "EPR":
                EPR += 1
            elif m == "EHD":
                EHD += 1
            else:
                INTRUSOS += 1
        print("EPR: {}\nEHD: {}\nINTRUSOS: {}".format(EPR,EHD,INTRUSOS))
    except EOFError:
        break