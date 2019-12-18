# -*- coding: utf-8 -*-
n = str(input())
nat = ['zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove']
dez = ['dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove']
dezenas = ['dez','vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']
centenas = ['cento','duzentos','trezentos','quatrocentos','quinhentos','seissentos','setessentos','oitossentos','novessentos']
saida = ""
num = int(n)

if len(n) == 1:
    pri = int(n[0])
    saida += nat[pri]
elif len(n) == 2:
    pri = int(n[0])
    sec = int(n[1])
    if pri == 1 and sec != 0:
        saida += dez[sec]
    elif pri == 1 and sec == 0:
        saida += dez[sec]
    else:
        saida += dezenas[pri-1]
        if sec != 0:
            saida += " e " + nat[sec]
elif len(n) == 3:
    pri = int(n[0])
    sec = int(n[1])
    ter = int(n[2])
    if pri == 1 and sec == 0 and ter == 0:
        saida += centenas[pri-1]
    else:
        saida += centenas[pri-1]
    if sec != 0:
        saida += " e " + dezenas[sec-1]
    if ter != 0:
        saida += " e " + nat[ter]
elif len(n) == 4:
    pri = int(n[0])
    sec = int(n[1])
    ter = int(n[2])
    qua = int(n[3])
    if pri!=1:
        saida += nat[pri] + " mil"
    else:
        saida += "mil"
    if sec != 0:
        saida += " e " + centenas[sec-1]
    if ter != 0:
        saida += " e " + dezenas[ter-1]
    if qua != 0:
        saida += " e " + nat[qua]
elif len(n) == 5:
    pri = int(n[0])
    sec = int(n[1])
    ter = int(n[2])
    qua = int(n[3])
    cin = int(n[4])
    a = ""
    if pri == 1 and sec != 0:
        a += dez[sec]
    elif pri == 1 and sec == 0:
        a += dez[sec]
    else:
        saida += dezenas[pri - 1]
        if sec != 0:
            a += " e " + nat[sec]
    saida += a + " mil"
    if ter != 0:
        saida += " e " + centenas[ter-1]
    if qua != 0:
        saida += " e " + dezenas[qua-1]
    if cin != 0:
        saida += " e " + nat[cin]
print(saida)