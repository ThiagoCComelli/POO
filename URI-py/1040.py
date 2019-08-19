# -*- coding: utf-8 -*-
n1 , n2, n3, n4 = map(float, input().split())
m = (n1*2+n2*3+n3*4+n4*1)/10

if m >= 7:
    print("Media: %.1f\nAluno aprovado" % m)
elif m <= 6.9 and m >= 5:
    print("Media: %.1f\nAluno em exame."%(m))
    ne = float(input())
    nf = (m + ne) / 2
    print("Nota do exame: %.1f"%ne)
    if nf == 5 or nf > 5:
        print("Aluno aprovado.\nMedia final: %.1f"%nf)

elif m < 5:
    print("Media: %.1f\nAluno reprovado" % m)
else:
    print("error")
