# -*- coding: utf-8 -*-
n = int(input())
tosaques = 0
tosaques1 = 0
tobloqueio = 0
tobloqueio1 = 0
toataques = 0
toataques1 = 0
totalpontos = 0
for i in range(n):
    nome = str(input())
    saques, bloqueios, ataques = map(int,input().split())
    saques1, bloqueios1, ataques1 = map(int,input().split())
    tosaques += saques
    tosaques1 += saques1
    tobloqueio += bloqueios
    tobloqueio1 += bloqueios1
    toataques += ataques
    toataques1 += ataques1
    totalpontos += ataques1 + bloqueios1 + saques1
print("Pontos de Saque: %.2f %%."%((tosaques1/tosaques)*100))
print("Pontos de Bloqueio: %.2f %%."%((tobloqueio1/tobloqueio)*100))
print("Pontos de Ataque: %.2f %%."%((toataques1/toataques)*100))
