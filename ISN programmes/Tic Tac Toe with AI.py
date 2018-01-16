# -*- coding: utf-8 -*-

"""
Created on Thu Jan 28 18:16:21 2016

@author: Aurian
"""

from tkinter import *
import random
 
r=int()
r,u,z,w=0,0,0,0
i,j=0,0

def player1():
    global z,w,fen,cavenas
    z=1
    fen1.destroy()
    fen=Tk()
    fen.title("Tic Tac Toe") # crée la fenetre principale
    cavenas=Canvas(fen,width=300,height=300,bg="white")
    cavenas.grid(row=0,column=0,columnspan=6)
    cavenas.create_line(0,4,300,4,width=3)
    cavenas.create_line(0,100,300,100,width=3)
    cavenas.create_line(0,200,300,200,width=3)
    cavenas.create_line(0,299,300,299,width=3)
    cavenas.create_line(4,0,4,300,width=3)
    cavenas.create_line(100,0,100,300,width=3)
    cavenas.create_line(200,0,200,300,width=3)
    cavenas.create_line(299,0,299,300,width=3)
    cavenas.bind("<Button-1>",clic)
    if z==0:
        boutton1=Button(fen,text="Annuler",command=annul)
        boutton1.grid(row=2,column=0)
    """fen.mainloop()"""
    w=1
    
def player2():
    global z,w,cavenas,fen
    z=0
    fen1.destroy()
    fen=Tk()
    fen.title("Tic Tac Toe") # crée la fenetre principale
    cavenas=Canvas(fen,width=300,height=300,bg="white")
    cavenas.grid(row=0,column=0,columnspan=6)
    cavenas.create_line(0,4,300,4,width=3)
    cavenas.create_line(0,100,300,100,width=3)
    cavenas.create_line(0,200,300,200,width=3)
    cavenas.create_line(0,299,300,299,width=3)
    cavenas.create_line(4,0,4,300,width=3)
    cavenas.create_line(100,0,100,300,width=3)
    cavenas.create_line(200,0,200,300,width=3)
    cavenas.create_line(299,0,299,300,width=3)
    cavenas.bind("<Button-1>",clic)
    if z==0:
        boutton1=Button(fen,text="Annuler",command=annul)
        boutton1.grid(row=2,column=0)
    """fen.mainloop()"""
    w=1
    
def clic(event): # fonction récupérant les coordonnées du clic et calculant à quelle case corespond le clic
    global i,j,r,tableau
    X=event.x
    Y=event.y
    i=X//100+1
    j=Y//100+1
    r=r+1
    if r%2!=1:
        rond(i,j)
    if r%2!=0:
        croix(i,j)
        
def rond(i,j): # fonction créant les ronds
    global r,tableau,cavenas
    if tableau[i-1][j-1]==0:
        liste.append(cavenas.create_oval((i-1)*100+20,(j-1)*100+20,(i-1)*100+80,(j-1)*100+80,width=3))
        liste_i.append(i)
        liste_j.append(j)
        tableau[i-1][j-1]=1
        gagne()
    else:
        print("La  case est déjà occupée")
        r=r-1

def croix(i,j): # fonction créant les croix
    global r,z,tableau,cavenas
    if z==0:
        if tableau[i-1][j-1]==0:
            liste.append(cavenas.create_line((i-1)*100+20,(j-1)*100+20,(i-1)*100+80,(j-1)*100+80,width=3))
            liste.append(cavenas.create_line((i-1)*100+80,(j-1)*100+20,(i-1)*100+20,(j-1)*100+80,width=3))
            liste_i.append(i)
            liste_j.append(j)
            tableau[i-1][j-1]=3
            gagne()
        else:
            print("La  case est déjà occupée")
            r=r-1
    if z==1:
        if tableau[i-1][j-1]==0:
           cavenas.create_line((i-1)*100+20,(j-1)*100+20,(i-1)*100+80,(j-1)*100+80,width=3)
           cavenas.create_line((i-1)*100+80,(j-1)*100+20,(i-1)*100+20,(j-1)*100+80,width=3)
           tableau[i-1][j-1]=3
           gagne()
           ia()
           
def gagne(): # fonction calculant si quelqu'un gagne la partie 
    global u,fen2
    if tableau[0][0]*tableau[1][0]*tableau[2][0]==1:
        u=2
    if tableau[0][1]*tableau[1][1]*tableau[2][1]==1:
        u=2
    if tableau[0][2]*tableau[1][2]*tableau[2][2]==1:
        u=2
    if tableau[0][0]*tableau[0][1]*tableau[0][2]==1:
        u=2
    if tableau[1][0]*tableau[1][1]*tableau[1][2]==1:
        u=2
    if tableau[2][0]*tableau[2][1]*tableau[2][2]==1:
        u=2
    if tableau[0][0]*tableau[1][1]*tableau[2][2]==1:
        u=2
    if tableau[2][0]*tableau[1][1]*tableau[0][2]==1:
        u=2
    if tableau[0][0]*tableau[1][0]*tableau[2][0]==27:
        u=3
    if tableau[0][1]*tableau[1][1]*tableau[2][1]==27:
        u=3
    if tableau[0][2]*tableau[1][2]*tableau[2][2]==27:
        u=3
    if tableau[0][0]*tableau[0][1]*tableau[0][2]==27:
        u=3
    if tableau[1][0]*tableau[1][1]*tableau[1][2]==27:
        u=3
    if tableau[2][0]*tableau[2][1]*tableau[2][2]==27:
        u=3
    if tableau[0][0]*tableau[1][1]*tableau[2][2]==27:
        u=3
    if tableau[2][0]*tableau[1][1]*tableau[0][2]==27:
        u=3
    if tableau[0][0]+tableau[0][1]+tableau[0][2]+tableau[1][0]+tableau[1][1]+tableau[1][2]+tableau[2][0]+tableau[2][1]+tableau[2][2]==19:
        u=1
    if u==0: # la partie est en cour
        u=u
    else: # crée la fenetre affichant le résultat de la partie et la possibilité de recommencer ou de quitter
        fen2=Tk()
        fen2.title("Résultat")
        if u==1:
            zone1=Label(fen2,text="Personne n'a gagné")
        if u==2:
            zone1=Label(fen2,text="Les ronds ont gagné !")
        if u==3:
            zone1=Label(fen2,text="Les croix ont gagné !")
        zone1.grid(row=0,column=0)
        boutton2=Button(fen2,text="Recommencer",command=recommencer)
        boutton2.grid(row=1,column=0)
        boutton3=Button(fen2,text="Quitter",command=quitter)
        boutton3.grid(row=2,column=0)
        fen2.mainloop()
        
def recommencer(): # fonction permettant de refaire une partie
    global r,u,tableau,liste,liste_i,liste_j
    cavenas.delete(ALL) # réinitialise la fenetre de jeu        
    cavenas.create_line(0,4,300,4,width=3)
    cavenas.create_line(0,100,300,100,width=3)
    cavenas.create_line(0,200,300,200,width=3)
    cavenas.create_line(0,299,300,299,width=3)
    cavenas.create_line(4,0,4,300,width=3)
    cavenas.create_line(100,0,100,300,width=3)
    cavenas.create_line(200,0,200,300,width=3)
    cavenas.create_line(299,0,299,300,width=3)        
    r,u=0,0 # réinitialise les variables de calclul permettant le bon fonctionnement du jeu
    tableau=[[0,0,0],[0,0,0],[0,0,0]]
    liste=[]
    liste_i=[]
    liste_j=[]
    fen2.destroy()
        
def quitter(): # fonction permettant de quitter le jeu
    global w,fen2,fen
    w=0
    fen2.destroy()
    fen.destroy() 
    
def annul(): # fonction permettant d'annuler la ou les dernière(s) action(s)
    global r,tableau
    i=liste_i[r-1]
    j=liste_j[r-1]
    tableau[i-1][j-1]=0
    liste_i.remove(liste_i[r-1])
    liste_j.remove(liste_j[r-1])
    if r%2==0: # supprime un rond
        cavenas.delete(liste[-1])
        liste.remove(liste[-1])
    if r%2!=0: # supprime une croix
        cavenas.delete(liste[-1])
        liste.remove(liste[-1])
        cavenas.delete(liste[-1])
        liste.remove(liste[-1])
    r=r-1
   
def ia(): # fonction permettant de jouer contre l'ordinateur
    global r,tableau,liste
    z=0
    tableau2=[]
    tableau2=tableau
    print("tableau2",tableau2)
    print("r ia 1",r)
    print("ia 1",tableau)
    if r<9:
        while z==0:
            i=random.randint(0,2)
            j=random.randint(0,2)
            print("i ia =",i)
            print("j ia=",j)
            if tableau[1][1]==0:
                cavenas.create_oval((1)*100+20,(1)*100+20,(1)*100+80,(1)*100+80,width=3)
                tableau[1][1]=1
                z=z+1
            if tableau[0][0]+tableau[1][0]+tableau[2][0]==2: # ici les rond vont essayer de gagner
                z=z
                while z==0:
                    i=random.randint(0,2)
                    j=0
                    if tableau[i][j]==0:
                        cavenas.create_oval((i)*100+20,(j)*100+20,(i)*100+80,(j)*100+80,width=3)
                        tableau[i][j]=1
                        z=z+1
                        gagne()        
                    else:                
                        print("IA again")
            if tableau[0][1]+tableau[1][1]+tableau[2][1]==2:
                z=z
                while z==0:
                    i=random.randint(0,2)
                    j=1
                    if tableau[i][j]==0:
                        cavenas.create_oval((i)*100+20,(j)*100+20,(i)*100+80,(j)*100+80,width=3)
                        tableau[i][j]=1
                        z=z+1
                        gagne()        
                    else:                
                        print("IA again")
            if tableau[0][2]+tableau[1][2]+tableau[2][2]==2:
                z=z
                while z==0:
                    i=random.randint(0,2)
                    j=2
                    if tableau[i][j]==0:
                        cavenas.create_oval((i)*100+20,(j)*100+20,(i)*100+80,(j)*100+80,width=3)
                        tableau[i][j]=1
                        z=z+1
                        gagne()        
                    else:                
                        print("IA again")
            if tableau[0][0]+tableau[0][1]+tableau[0][2]==2:
                z=z
                while z==0:
                    j=random.randint(0,2)
                    i=0
                    if tableau[i][j]==0:
                        cavenas.create_oval((i)*100+20,(j)*100+20,(i)*100+80,(j)*100+80,width=3)
                        tableau[i][j]=1
                        z=z+1
                        gagne()        
                    else:                
                        print("IA again")
            if tableau[1][0]+tableau[1][1]+tableau[1][2]==2:
                z=z
                while z==0:
                    j=random.randint(0,2)
                    i=1
                    if tableau[i][j]==0:
                        cavenas.create_oval((i)*100+20,(j)*100+20,(i)*100+80,(j)*100+80,width=3)
                        tableau[i][j]=1
                        z=z+1
                        gagne()        
                    else:                
                        print("IA again")
            if tableau[2][0]+tableau[2][1]+tableau[2][2]==2:
                z=z
                while z==0:
                    j=random.randint(0,2)
                    i=2
                    if tableau[i][j]==0:
                        cavenas.create_oval((i)*100+20,(j)*100+20,(i)*100+80,(j)*100+80,width=3)
                        tableau[i][j]=1
                        z=z+1
                        gagne()        
                    else:                
                        print("IA again")
            if tableau[0][0]+tableau[1][1]+tableau[2][2]==2:
                z=z
                if tableau[0][0]==0:
                    cavenas.create_oval((0)*100+20,(0)*100+20,(0)*100+80,(0)*100+80,width=3)
                    tableau[0][0]=1
                    z=z+1
                    gagne()        
                else:                
                    print("IA again")
                z=z
                if tableau[1][1]==0:
                    cavenas.create_oval((1)*100+20,(1)*100+20,(1)*100+80,(1)*100+80,width=3)
                    tableau[1][1]=1
                    z=z+1
                    gagne()        
                else:                
                    print("IA again")
                z=z
                if tableau[2][2]==0:
                    cavenas.create_oval((2)*100+20,(2)*100+20,(2)*100+80,(2)*100+80,width=3)
                    tableau[2][2]=1
                    z=z+1
                    gagne()        
                else:                
                    print("IA again")
            if tableau[2][0]+tableau[1][1]+tableau[0][2]==2:
                z=z
                if tableau[2][0]==0:
                    cavenas.create_oval((2)*100+20,(0)*100+20,(2)*100+80,(0)*100+80,width=3)
                    tableau[2][0]=1
                    z=z+1
                    gagne()        
                else:                
                    print("IA again")
                z=z
                if tableau[1][1]==0:
                    cavenas.create_oval((1)*100+20,(1)*100+20,(1)*100+80,(1)*100+80,width=3)
                    tableau[1][1]=1
                    z=z+1
                    gagne()        
                else:                
                    print("IA again")
                z=z
                if tableau[0][2]==0:
                    cavenas.create_oval((0)*100+20,(2)*100+20,(0)*100+80,(2)*100+80,width=3)
                    tableau[0][2]=1
                    z=z+1
                    gagne()        
                else:                
                    print("IA again")
            if tableau[0][0]+tableau[1][0]+tableau[2][0]==6: # ici les rond empechent les croix de gagner
                z=z
                while z==0:
                    i=random.randint(0,2)
                    j=0
                    if tableau[i][j]==0:
                        cavenas.create_oval((i)*100+20,(j)*100+20,(i)*100+80,(j)*100+80,width=3)
                        tableau[i][j]=1
                        z=z+1
                        gagne()        
                    else:                
                        print("IA again")
            if tableau[0][1]+tableau[1][1]+tableau[2][1]==6:
                z=z
                while z==0:
                    i=random.randint(0,2)
                    j=1
                    if tableau[i][j]==0:
                        cavenas.create_oval((i)*100+20,(j)*100+20,(i)*100+80,(j)*100+80,width=3)
                        tableau[i][j]=1
                        z=z+1
                        gagne()        
                    else:                
                        print("IA again")
            if tableau[0][2]+tableau[1][2]+tableau[2][2]==6:
                z=z
                while z==0:
                    i=random.randint(0,2)
                    j=2
                    if tableau[i][j]==0:
                        cavenas.create_oval((i)*100+20,(j)*100+20,(i)*100+80,(j)*100+80,width=3)
                        tableau[i][j]=1
                        z=z+1
                        gagne()        
                    else:                
                        print("IA again")
            if tableau[0][0]+tableau[0][1]+tableau[0][2]==6:
                z=z
                while z==0:
                    j=random.randint(0,2)
                    i=0
                    if tableau[i][j]==0:
                        cavenas.create_oval((i)*100+20,(j)*100+20,(i)*100+80,(j)*100+80,width=3)
                        tableau[i][j]=1
                        z=z+1
                        gagne()        
                    else:                
                        print("IA again")
            if tableau[1][0]+tableau[1][1]+tableau[1][2]==6:
                z=z
                while z==0:
                    j=random.randint(0,2)
                    i=1
                    if tableau[i][j]==0:
                        cavenas.create_oval((i)*100+20,(j)*100+20,(i)*100+80,(j)*100+80,width=3)
                        tableau[i][j]=1
                        z=z+1
                        gagne()        
                    else:                
                        print("IA again")
            if tableau[2][0]+tableau[2][1]+tableau[2][2]==6:
                z=z
                while z==0:
                    j=random.randint(0,2)
                    i=2
                    if tableau[i][j]==0:
                        cavenas.create_oval((i)*100+20,(j)*100+20,(i)*100+80,(j)*100+80,width=3)
                        tableau[i][j]=1
                        z=z+1
                        gagne()        
                    else:                
                        print("IA again")
            if tableau[0][0]+tableau[1][1]+tableau[2][2]==6:
                z=z
                if tableau[0][0]==0:
                    cavenas.create_oval((0)*100+20,(0)*100+20,(0)*100+80,(0)*100+80,width=3)
                    tableau[0][0]=1
                    z=z+1
                    gagne()        
                else:                
                    print("IA again")
                z=z
                if tableau[1][1]==0:
                    cavenas.create_oval((1)*100+20,(1)*100+20,(1)*100+80,(1)*100+80,width=3)
                    tableau[1][1]=1
                    z=z+1
                    gagne()        
                else:                
                    print("IA again")
                z=z
                if tableau[2][2]==0:
                    cavenas.create_oval((2)*100+20,(2)*100+20,(2)*100+80,(2)*100+80,width=3)
                    tableau[2][2]=1
                    z=z+1
                    gagne()        
                else:                
                    print("IA again")
            if tableau[2][0]+tableau[1][1]+tableau[0][2]==6:
                z=z
                if tableau[2][0]==0:
                    cavenas.create_oval((2)*100+20,(0)*100+20,(2)*100+80,(0)*100+80,width=3)
                    tableau[2][0]=1
                    z=z+1
                    gagne()        
                else:                
                    print("IA again")
                z=z
                if tableau[1][1]==0:
                    cavenas.create_oval((1)*100+20,(1)*100+20,(1)*100+80,(1)*100+80,width=3)
                    tableau[1][1]=1
                    z=z+1
                    gagne()        
                else:                
                    print("IA again")
                z=z
                if tableau[0][2]==0:
                    cavenas.create_oval((0)*100+20,(2)*100+20,(0)*100+80,(2)*100+80,width=3)
                    tableau[0][2]=1
                    z=z+1
                    gagne()        
                else:                
                    print("IA again")                
            if z==0:
                if tableau[i][j]==0:
                    liste.append(cavenas.create_oval((i)*100+20,(j)*100+20,(i)*100+80,(j)*100+80,width=3))
                    tableau[i][j]=1
                    z=z+1
                    gagne()        
                else:                
                    print("IA again")
    else:
        gagne()
    r=r+1  
  
tableau=[[0,0,0],[0,0,0],[0,0,0]]
liste=[] # fonctio qui enregistre les croix et les ronds pour la fonction annul
liste_i=[] # fonction qui enregistre i pour pouvoir remettre les valeur de tableau=[] à 0
liste_j=[] # fonction qui enregistre j pour pouvoir remettre les valeur de tableau=[] à 0
fen1=Tk() # choisir mode 1 joueur ou mode 2 joueurs
fen1.title("Menu")
boutton4=Button(fen1,text="Mode 1 joueur",command=player1)
boutton4.grid(row=0,column=0)
boutton5=Button(fen1,text="Mode 2 joueurs",command=player2)
boutton5.grid(row=1,column=1)
fen1.mainloop()



if w==1:
    fen=Tk()
    fen.title("Tic Tac Toe") # crée la fenetre principale
    cavenas=Canvas(fen,width=300,height=300,bg="white")
    cavenas.grid(row=0,column=0,columnspan=6)
    cavenas.create_line(0,4,300,4,width=3)
    cavenas.create_line(0,100,300,100,width=3)
    cavenas.create_line(0,200,300,200,width=3)
    cavenas.create_line(0,299,300,299,width=3)
    cavenas.create_line(4,0,4,300,width=3)
    cavenas.create_line(100,0,100,300,width=3)
    cavenas.create_line(200,0,200,300,width=3)
    cavenas.create_line(299,0,299,300,width=3)
    cavenas.bind("<Button-1>",clic)
    if z==0:
        boutton1=Button(fen,text="Annuler",command=annul)
        boutton1.grid(row=2,column=0)
    fen.mainloop()