# -*- coding: utf-8 -*-
d = input().split()
tu = 0
ji = 0
while d[0] != "ABEND":
    d[1] = int(d[1])
    if d[0] == "SALIDA":
        tu += d[1]
        ji += 1
    else:
        tu -= d[1]
        ji -= 1
    d = input().split()
print(tu)
print(ji)
