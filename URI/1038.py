# -*- coding: utf-8 -*-
cod, qua = input().split()
cod,  qua = int(cod), int(qua)
if cod == 1:
    total = qua * 4
elif cod == 2:
    total = qua * 4.5
elif cod == 3:
    total = qua * 5
elif cod == 4:
    total = qua * 2
elif cod == 5:
    total = qua * 1.5

print("Total: R$ %.2f" % total)
