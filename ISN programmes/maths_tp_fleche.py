# -*- coding: utf-8 -*-
from random import *
n=int(input("Entrez le nombre de fois que l'on va effectuer le jeu"))
i=float()
j=float()
z=float()
b,r,z=0,0,0
while b<n:
    i=random()
    j=random()
    b=b+1
    if (j/i)<1:
        r=r+1
z=((r/b)*100)
print("la probabilité de gagner est de",z,"% pour",n,"essais")