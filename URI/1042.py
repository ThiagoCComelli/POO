# -*- coding: utf-8 -*-
a, b, c = map(int, input().split())
if a>b>c:
    print("%d\n%d\n%d" % (c, b, a))
elif a>c>b:
    print("%d\n%d\n%d" % (b, c, a))
elif b>a>c:
    print("%d\n%d\n%d" % (c, a, b))
elif b>c>a:
    print("%d\n%d\n%d" % (a, c, b))
elif c>a>b:
    print("%d\n%d\n%d" % (b, a, c))
elif c>b>a:
    print("%d\n%d\n%d" % (a, b, c))

print("\n%d\n%d\n%d"%(a,b,c))
