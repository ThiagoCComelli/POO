# -*- coding: utf-8 -*-
flavio = [int(x) for x in input().split()]
aposta = [int(x) for x in input().split()]
t = 0
for i in flavio:
    if i in aposta:
        t += 1
if t < 3:
    print('azar')
elif t == 3:
    print('terno')
elif t == 4:
    print('quadra')
elif t == 5:
    print('quina')
elif t == 6:
    print('sena')