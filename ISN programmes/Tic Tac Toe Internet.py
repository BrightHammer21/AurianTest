# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 21:29:36 2016

@author: Aurian
"""

from tkinter import *
fen1 = Tk()
tex1 = Label(fen1, text='Bienvenue dans Tic Tac Toe', fg='pink')
tex1.pack()
bou1 = Button(fen1, text='Quitter', command = fen1.destroy)
bou1.pack()
canvas = Canvas(fen1, width=300, height=300, background='pink')
ligne1 = canvas.create_line(100, 0, 100, 300)
ligne2 = canvas.create_line(0, 200, 300, 200)
ligne3 = canvas.create_line(200,0,200,300)
ligne4 = canvas.create_line(0,100,300,100)
carre1 = canvas.create_rectangle(0,0,100,100)
carre2 = canvas.create_rectangle(100,0,200,100)
carre3 = canvas.create_rectangle(200,0,300,100)
carre4 = canvas.create_rectangle(0,100,100,200)
carre5 = canvas.create_rectangle(100,100,200,200)
carre6 = canvas.create_rectangle(200,100,300,200)
carre7 = canvas.create_rectangle(0,200,100,300)
carre8 = canvas.create_rectangle(100,200,200,300)
carre9 = canvas.create_rectangle(200,200,300,300)

canvas.pack()

def player():
    player == carre is blue
    computer == carre is white

def board_full():
    if None not in board:
        return True
    else:
        return False

def possible_moves():
    possible_moves = []
    for i in range (0,8):
        if board [i] is None:
            possible_moves.append(i)
        else :
            pass
        return possible_moves
def pc_move():
    m = True
    while m:
        pc_move = random.randint(0,8)
        if pc_move in possible_moves():
            board[pc_move] = 'O'
            canvas.itemconfigure(tagOrId=(pc_move + 1),fill='white')
    
canvas.bind("<Button-1>",player)
board = [None, None, None, None, None, None, None, None, None]
map = { (0,0): 0, (0,1): 1, (0,2): 2, (1,0): 3, (1,1): 4, (1,2): 5, (2,0): 6, (2,1): 7, (2,2): 8}

def draw_out():
    print(board[0:3])
    print(board[3:6])
    print(boars[6:9])

def play(event):
    print ('clicked', event.y, event.x)
    cx = canvas.canvasx(event.x)
    cy = canvas.canvasy(event.y)
    cid = canvas.find_closest(cx,cy)[0]
    my_move =  map[(cy // block_size, cx // block_size)]
    if board[my_move] is None :
        board[my_move] = "x"
        canvas.itemconfigure(cid,fill='blue')
    else :
        return None

    draw_out()
    if check_game() is not None:
        print(check_game() )
    else:
        pass
    possible_moves()
    pc_move()
    draw_out()
    if check_game() is not None:
        print(check_game() )
    else:
        pass
    return

def check_game(self):
        """
        Check if the game is win or lost or a tie
        Return:  win, lose, tie, none """
        result=None
        if (self.board[0] == self.board[1] == self.board[2] == 'X') or (
                            self.board[3] == self.board[4] == self.board[5] == 'X') or (
                            self.board[6] == self.board[7] == self.board[8] == 'X') or (
                            self.board[0] == self.board[3] == self.board[6] == 'X') or (
                            self.board[1] == self.board[4] == self.board[7] == 'X') or (
                            self.board[2] == self.board[5] == self.board[8] == 'X') or (
                            self.board[0] == self.board[4] == self.board[8] == 'X') or (
                            self.board[2] == self.board[4] == self.board[6] == 'X'):
            result = 'tu as gagner!'  # player win
            self.my_lbl.configure(text=result)
        elif (self.board[0] == self.board[1] == self.board[2] == 'O') or (
                            self.board[3] == self.board[4] == self.board[5] == 'O') or (
                            self.board[6] == self.board[7] == self.board[8] == 'O') or (
                            self.board[0] == self.board[3] == self.board[6] == 'O') or (
                            self.board[1] == self.board[4] == self.board[7] == 'O') or (
                            self.board[2] == self.board[5] == self.board[8] == 'O') or (
                            self.board[0] == self.board[4] == self.board[8] == 'O') or (
                            self.board[2] == self.board[4] == self.board[6] == 'O'):
            result = 'tu as perdu!'  # player lose
            self.my_lbl.config(text=result)
        elif self.board_full()is True:
                result = 'match nul!'  # tie
                self.my_lbl.configure(text=result)
        else:
            pass
        return result

def restart ():
    initialize_game()
    fen1.mainloop()
