# -*- coding: utf-8 -*-
def fib (n):
    global cont
    cont += 1
    if n < 2:
        return 1
    return fib (n -1) + fib (n -2)
n = int(input())
for i in range(n):
    cont = 0
    f = int(input())
    f1 = fib(f)
    print("fib({}) = {} calls = {}".format(f,cont-1,f1))