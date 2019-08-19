tamanho = int(input())
tamanho1 = tamanho
pedacos = 0
cont = 1

while (tamanho/2)>=2:
    tamanhon = tamanho/2
    if tamanhon>=2:
        cont += 1
    pedacos = 4**cont
    tamanho = tamanhon
if tamanho1==2:
    pedacos = 4 ** 1
print(pedacos)
