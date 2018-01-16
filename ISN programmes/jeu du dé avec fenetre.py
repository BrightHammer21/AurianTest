# Créé par aurian.durand, le 16/12/2015 en Python 3.2
from tkinter import *
import random
fen=Tk()
fen.title("Jeu du dé")
label=Label(fen,text="Résultat du dé")
label.pack(side=BOTTOM)
d=0
def fonction1():
    d=random.randint(1,6)
    label.configure(text=d)
    return
bouton1=Button(fen,text='lance le dé',command=fonction1)
bouton1.pack(side=TOP)
fen.mainloop()