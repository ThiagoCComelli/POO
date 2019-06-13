# -*- coding: utf-8 -*-
import math
a, b, c = map(float, input().split())
x = (b**2)-(4*a*c)
if x > 0:
    if a > 0:
        x = math.sqrt(x)
        x1 = (-b + x) / (2 * a)
        x2 = (-b - x) / (2 * a)
        print("R1 = %.5f\nR2 = %.5f" % (x1, x2))
    else:
        print("Impossivel calcular")
elif x < 0:
    print("Impossivel calcular")
else:
    x1 = (-b + x) / (2 * a)
    x2 = (-b - x) / (2 * a)
    print("R1 = %.5f\nR2 = %.5f" % (x1, x2))
