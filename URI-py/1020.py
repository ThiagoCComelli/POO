# -*- coding: utf-8 -*-
dias = int(input())
anos = dias//365
meses = (dias%365)//30
dias = (dias%365)%30
print("%d ano(s)\n%d mes(es)\n%d dia(s)"% (anos, meses, dias))
