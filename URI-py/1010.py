# -*- coding: utf-8 -*-
x1, x2, x3 = input().split()
y1, y2, y3 = input().split()
x2 = int(x2)
x3 = float(x3)
y2 = int(y2)
y3 = float(y3)
t = x2 * x3 + y2 * y3
print("VALOR A PAGAR: R$ %.2f" % t)

