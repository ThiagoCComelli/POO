andares , cap = map(int,input().split())
pes = 0
acima = 0
for i in range (andares):
    saiu, entrou = map(int,input().split())
    pes += (entrou-saiu)
    if pes>cap:
        acima += 1
if acima != 0:
    print("S")
else:
    print("N")
