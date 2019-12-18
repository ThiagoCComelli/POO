# -*- coding: utf-8 -*-
qtde = 0
val = []
while True:
    n = float(input())
    if n == 0:
        break
    val.append(n)
    qtde += 1
sorted(val)
print("SOMA: {}".format(sum(val)))
print("QTDE: {}".format(len(val)))
print("MEDIA: {}".format(sum(val)/len(val)))
print("MAIOR: {}".format(max(val)))
print("MENOR: {}".format(min(val)))