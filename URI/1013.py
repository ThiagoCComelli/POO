# -*- coding: utf-8 -*-
import math
valor = input().split()
x, y, z = valor
maiorab = ((int(x)+int(y)+abs(int(x)-int(y))))/2
resul = (int(maiorab)+int(z)+abs(int(maiorab)-int(z)))/2
print("%d eh o maior" % resul)
