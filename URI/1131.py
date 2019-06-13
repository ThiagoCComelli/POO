# -*- coding: utf-8 -*-

inte = 0
gre = 0
emp = 0
novo = 1
qtde = 0
while novo == 1:
    x, y = map(int, input().split())
    qtde += 1
    if x > y:
        inte += 1
    elif y > x:
        gre += 1
    else:
        emp += 1
    novo = int(input("Novo grenal (1-sim 2-nao)"))
print("%d grenais"%qtde)
print("Inter:%d"%inte)
print("Gremio:%d"%gre)
print("Empates:%d"%emp)

if inte>gre:
    print("Inter venceu mais")
elif inte<gre:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
