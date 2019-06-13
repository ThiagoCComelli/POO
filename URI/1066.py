# -*- coding: utf-8 -*-
lista = []
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
par = 0
imp = 0
neg = 0
pos = 0
for n in lista:
    if n%2==0:
        par += 1
    else:
        imp += 1
    if n > 0:
        pos += 1
    else:
        if n < 0:
            neg += 1
print("%d valor(es) par(es)" %par)
print("%d valor(es) impar(es)" %imp)
print("%d valor(es) positivo(s)" %pos)
print("%d valor(es) negativo(s)" %neg)
