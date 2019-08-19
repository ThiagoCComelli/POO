# -*- coding: utf-8 -*-
qtd = "1"
while True:
    n = input().split()
    r = ""
    if n[0] == "0" and n[1] == "0":
        break
    for i in n[1]:
        if i != n[0]:
            r += i
    if r == "" or int(r) == 0:
        r = "0"
    print(int(r))
