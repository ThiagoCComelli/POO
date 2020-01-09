# -*- coding: utf-8 -*-
n = str(input())
nat = ['zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove']
dez = ['dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove']
dezenas = ['dez','vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']
centenas = ['cem','duzentos','trezentos','quatrocentos','quinhentos','seissentos','setessentos','oitossentos','novessentos']
num = int(n)
if len(n) == 1:
    last = int(n[-1])
elif len(n) == 2:
    last = int(n[-1])
    last1 = int(n[-2])
elif len(n) == 3:
    last = int(n[-1])
    last1 = int(n[-2])
    last2 = int(n[-3])
elif len(n) == 4:
    last = int(n[-1])
    last1 = int(n[-2])
    last2 = int(n[-3])
    last3 = int(n[-4])
elif len(n) == 5:
    last = int(n[-1])
    last1 = int(n[-2])
    last2 = int(n[-3])
    last3 = int(n[-4])
    last4 = int(n[-5])
if num < 20 and num >= 0:
    if num >= 10:
        print(dez[last])
    else:
        print(nat[num])
elif num >= 20 and num < 100:
    if last==0:
        print(dezenas[last1-1])
    else:
        print(dezenas[last1-1] + " e " + nat[last])
elif num >= 100 and num < 1000:
    if last==0 and last1==0:
        print(centenas[num+(-num+1)])
    elif last==0:
        print(centenas[num+(-num+last2)-1] + " e " + dezenas[last1-1])
    elif last1==0:
        print(centenas[num+(-num+last2)-1] + " e " + nat[last])
    else:
        print(centenas[num + (-num + last2) - 1] + " e " + dezenas[last1 - 1] + " e " + nat[last])
elif num >= 1000 and num < 10000:

