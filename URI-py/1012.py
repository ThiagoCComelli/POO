# -*- coding: utf-8 -*-
linha = input().split()
a, b, c = linha
pi = 3.14159
tri = (float(a)*float(c))/2
cir = pi*(float(c)**2)
tra = ((float(a)+float(b))*float(c))/2
qua = float(b)**2
ret = float(a)*float(b)
print("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f" % (tri, cir, tra, qua, ret))
