# -*- coding: utf-8 -*-
s = float(input())
if s >= 0 and s <= 400:
    s1 = s*1.15
    r1 = s*.15
    p1 = ("15 %")
    print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %s"%(s1,r1,p1))
elif s > 400 and s <= 800:
    s2 = s*1.12
    r2 = s*.12
    p2 = ("12 %")
    print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %s"%(s2,r2,p2))
elif s >= 800.01 and s <= 1200:
    s3 = s*1.1
    r3 = s*.1
    p3 = ("10 %")
    print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %s"%(s3,r3,p3))
elif s >= 1200.01 and s <= 2000:
    s4 = s*1.07
    r4 = s*.07
    p4 = ("7 %")
    print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %s"%(s4,r4,p4))
else:
    s5 = s*1.04
    r5 = s*.04
    p5 = ("4 %")
    print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %s"%(s5,r5,p5))
