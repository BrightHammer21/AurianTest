# Créé par aurian.durand, le 23/11/2015 en Python 3.2
import random
r = random.randint(1,3)
e=input("Entrez le nombre de fois que l'on va reproduire le jeu")
e=int(e)
n=0
n=int(n)
changer=0
garder=0
##print(r)
while n<e:
    if r==3:
##    print(2)
        garder=garder+0
        changer=changer+1
    if r==2:
##    print(3)
        garder=garder+0
        changer=changer+1
    if r==1:
##    print(2)
        garder=garder+1
        changer=changer+0
    n=n+1
print("garder=",garder)
print("changer=",changer)