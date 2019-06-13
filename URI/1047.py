# -*- coding: utf-8 -*-
hi, mi, hf, mf = map(int,input().split())
hdd = hi-hf
if (hi==hf) and (mi==mf):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif hdd==(-1) and mi > mf:
    md = (60-mi)+mf
    print("O JOGO DUROU 0 HORA(S) E %d MINUTO(S)" %(abs(md)))
elif hi < hf:
    if mi > mf:
        md = (60-mi)+mf
    elif mi < mf:
        md = mf - mi
    elif mi == mf:
        md = mf - mi
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(hf-hi,abs(md)))
elif hi==hf and mi>mf:
    md = (60-mi)+mf
    print("O JOGO DUROU 23 HORA(S) E %d MINUTO(S)" % (abs(md)))
elif hi==hf and mf>mi:
    md = mf-mi
    print("O JOGO DUROU 0 HORA(S) E %d MINUTO(S)" % (abs(md)))
'''
elif hi > hf:
    if mi > mf:
        md = mf-mi
    elif mi < mf:
        md = mf-mi
    elif mi == mf:
        md = mf-mi
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)33" %(abs(hf-hi),abs(md)))
'''
'''
hi, mi, hf, mf = map(int,input().split())
hdd = hi-hf
if (hi==hf) and (mi==mf):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif hdd==(-1) and mi > mf:
    md = (60-mi)+mf
    print("O JOGO DUROU 0 HORA(S) E %d MINUTO(S)22" %(abs(md)))
elif hi < hf:
    if mi > mf:
        md = (60-mi)+mf
    elif mi < mf:
        md = mf - mi
    elif mi == mf:
        md = mf - mi
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)44" %(hf-hi,abs(md)))
elif hi==hf and mi>mf:
    md = (60-mi)+mf
    print("O JOGO DUROU 0 HORA(S) E %d MINUTO(S)55" % (abs(md)))
elif hi==hf and mf>mi:
    md = mf-mi
    print("O JOGO DUROU 0 HORA(S) E %d MINUTO(S)66" % (abs(md)))
'''
