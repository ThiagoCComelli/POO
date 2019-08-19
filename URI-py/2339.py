# -*- coding: utf-8 -*-
#c= competidores
#p= folhas
#F= folhas pra cada
c, p, f = map(int, input().split())
fn = c * f
if fn == p or fn < p:
    print("S")
else:
    print("N")
