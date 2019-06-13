dia, saldo = map(int,input().split())
lista = []
novo = 0
novo += saldo
for i in range(dia):
    saldonovo = int(input())
    novo += saldonovo
    lista.append(novo)
print(min(lista))
