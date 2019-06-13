# -*- coding: utf-8 -*-
cv,ce,cs,fv,fe,fs = map(int,input().split())
v, e = 3, 1
C = cv*3 + ce*1
F = fv*3 + fe*1
if C > F:
    print("C")
elif C < F:
    print("F")
elif C == F:
    if cs > fs:
        print("C")
    elif cs < fs:
        print("F")
    elif cs == fs:
        print("=")
