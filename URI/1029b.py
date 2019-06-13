# -*- coding: utf-8 -*-
def fib (n):
    global cont
    cont += 1
    return n if n <= 1 else fib(n - 2) + fib(n - 1)
n = int(input())
for i in range(n):
    cont = 0
    f = int(input())
    f1 = fib(f)
    print("fib({}) = {} calls = {}".format(f,cont-1,f1))