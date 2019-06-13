# -*- coding: utf-8 -*-
i = 1
j = 7
while i < 10:
    for u in range(3):
        print('I={} J={}'.format(i,j))
        j -= 1
    j += 5
    i += 2