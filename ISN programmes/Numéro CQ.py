# Créé par aurian.durand, le 23/09/2015 en Python 3.2
from tkinter import *
fen=Tk()
fen.title("Numéro de CQ")
fen.mainloop()
a=input("Entrez votre votre numéro de sécurité")
d=len(a)
d=int(d)
while d!=15:
    a=input("Code invalide, rentrez le à nouveau")
    d=len(a)
    d=int(d)
b=a[0:13]
b=int(b)
c=a[13:15]
c=int(c)
print(a)
print(b)
print(c)
if 97-b%97==c:
    print("Code bon")
if 97-b%97!=c:
    print("Code invalide")
