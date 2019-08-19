# -*- coding: utf-8 -*-
n = int(input())
r, s, c, nume = 0, 0, 0, 0
for _ in range(n):
    qua, tip = input().split()
    tip = str(tip)
    qua = int(qua)
    nume += qua
    if tip == "C":
        c += qua
    elif tip == "R":
        r += qua
    elif tip == "S":
        s += qua
print('Total: %d cobaias' %nume)
print('Total de coelhos: %d' %c)
print('Total de ratos: %d' %r)
print('Total de sapos: %d' %s)
print('Percentual de coelhos: %.2f' %float(((100*c)/nume)),'%')
print('Percentual de ratos: %.2f' %float(((100*r)/nume)),'%')
print('Percentual de sapos: %.2f' %float(((100*s)/nume)),'%')
