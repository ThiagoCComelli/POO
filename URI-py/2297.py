teste = 1
while True:
    n = int(input())
    if n == 0:
        break
    elif n != 0:
        aldo = 0
        beto = 0
        for i in range(n):
            aldo, beto = map(int,input().split())
            aldo += aldo
            beto += beto
        print("Teste %d"%teste)
        teste += 1
        if aldo>beto:
            print("Aldo")
        elif beto>aldo:
            print("Beto")
        print("")

