# -*- coding: utf-8 -*-
d = float(input())
if 0 < d <=2000:
    print("Isento")
elif 2000<d<=3000:
    v = d - 2000
    t = v*.08
    print("R$ %.2f"%t)
elif 3000<d<=4500:
    v = d - 3000
    t = (v*.18)+(1000*.08)
    print("R$ %.2f"%t)
elif d>4500:
    v = d - 4500
    t = (v * .28) + (1000 * .08) + (1500 * .18)
    print("R$ %.2f"%t)
