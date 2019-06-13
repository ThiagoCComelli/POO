# -*- coding: utf-8 -*-
while True:
  lista = []
  x = int(input())
  if(x == 0):
    break
  else:
    for i in range(1, x + 1):
      lista.append(i)
    print(' '.join(map(str, lista)))
