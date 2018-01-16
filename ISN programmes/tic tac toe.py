# Créé par aurian.durand, le 13/01/2016 en Python 3.2
from tkinter import *

global r
r=int()
r=0

def clic(event):
    global X
    global Y
    X=event.x
    Y=event.y
    r=0
    r=r+1
    print(r)
    rond()
        
def croix():
    cavenas.create_line(X-30,Y-30,X+30,Y+30,width=3)
    cavenas.create_line(X-30,Y+30,X+30,Y-30,width=3)

def rond():
    cavenas.create_oval(X-30,Y-30,X+30,Y+30,width=3)

fen=Tk()
fen.title("Tic Tac Toe")
cavenas=Canvas(fen, width=300,height=300,bg="white")
cavenas.grid(row=0, column=0, columnspan=6)
cavenas.create_line(0,3,300,3,width=3)
cavenas.create_line(0,100,300,100,width=3)
cavenas.create_line(0,200,300,200,width=3)
cavenas.create_line(0,298,300,298,width=3)
cavenas.create_line(3,0,3,300,width=3)
cavenas.create_line(100,0,100,300,width=3)
cavenas.create_line(200,0,200,300,width=3)
cavenas.create_line(298,0,298,300,width=3)
carre1=cavenas.create_rectangle(0,0,100,100,fill="blue")
carre2=cavenas.create_rectangle(100,0,200,100,fill="green")
carre3=cavenas.create_rectangle(200,0,300,100,fill="red")
carre4=cavenas.create_rectangle(0,200,100,100,fill="pink")
carre5=cavenas.create_rectangle(100,200,200,100,fill="blue")
carre6=cavenas.create_rectangle(200,100,300,200,fill="green")
carre7=cavenas.create_rectangle(0,200,100,300,fill="red")
carre8=cavenas.create_rectangle(100,200,200,300,fill="pink")
carre9=cavenas.create_rectangle(200,200,300,300,fill="yellow")
fenetre1=cavenas.create_windows(0,0,100,100,fill="yellow")





cavenas.bind("<Button-1>",clic)


fen.mainloop()
