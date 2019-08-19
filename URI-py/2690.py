# -*- coding: utf-8 -*-
na = int(input())
G=Q=a=k=u = 0
I=S=b=l=v = 1
E=O=Y=c=m=w = 2
F=P=Z=d=n=x = 3
J=T=e=o=y = 4
D=N=X=f=p=z = 5
A=K=U=g=q = 6
C=M=W=h=r = 7
B=L=V=i=s = 8
H=R=j=t = 9
for i in range(n):
    lista = []
    frase = str(input())
    for u in frase:
        for o in u:
            frase[o] = 4

