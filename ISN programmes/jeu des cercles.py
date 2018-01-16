# Créé par aurian.durand, le 16/12/2015 en Python 3.2

from tkinter import *
from PIL import ImageGrab
#import tkinter.colorchooser
import random

def fonction1(): #fonction qui suprimne le contenu de la fenetre#
    cavenas.delete(ALL)

def fonction2(): #fonction qui crée un cercle#
    a=b=random.randint(0,750)
    c=d=random.randint(0,750)
    cavenas.create_oval(a,b,c,d,width=5,fill="red",outline="blue")

def clic(event): #fonction du clic#
    global couleur0
    global couleur1
    X=event.x
    Y=event.y
    cavenas.create_oval(X-10, Y-10,X+10, Y+10,width=5,outline=couleur1, fill=couleur0)

def couleurFill(): #fonction pour choisir la couleur du remplissage#
    global couleur0
    (rouge0, vert0, bleu0), couleur0=tkinter.colorchooser.askcolor()

def couleurOutline(): #fonction pour choisir la couleur du contour#
    global couleur1
    (rouge0, vert0, bleu0), couleur1=tkinter.colorchooser.askcolor()

couleur0=''
couleur1=''

fen=Tk()
fen.title("Jeu du cercle")
cavenas=Canvas(fen, width=1000,height=500,bg="white") #crée la fenetre#
cavenas.grid(row=0, column=0, columnspan=6)

bouton1=Button(fen,text="Supprimer la fenêtre",command=fonction1) #bouton pour suprimer la fenetre#
bouton1.grid(row=1,column=1,sticky=W)

bouton2=Button(fen,text="Créer un cercle",command=fonction2) #bouton pour créer un cercle#
bouton2.grid(row=1,column=2,sticky=E)

bouton3=Button(fen,text='Sélectionner une couleur de remplissage',command=couleurFill) #bouton pour choisir une couleur de remplissage#
bouton3.grid(row=1,column=3,sticky=E)

bouton4=Button(fen,text='Sélectionner une couleur de contour',command=couleurOutline) #bouton pour choisir une couleur de contour#
bouton4.grid(row=1,column=4, sticky=E)


cavenas.bind("<Button-1>",clic)
fen.mainloop()