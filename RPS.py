from tkinter import *
import random
import tkinter

user = int
computer = int
win = 0
lose = 0

def game(win, lose, user):
    computer = random.randrange(1,4)
    if user == computer:
        var.set("It's a draw. \n No Points")  
    elif user == 1 and computer == 2:
        var.set("You chose Rock, I chose Paper. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)    
    elif user == 1 and computer == 3:
        var.set("You chose Rock, I chose Scissors. \nYou win")
        wins.set(wins.get() + 1)    
    elif user == 2 and computer == 1:
        var.set("You chose Paper, I chose Rock. \nYou win")
        wins.set(wins.get() + 1)
    elif user == 2 and computer == 3:
        var.set("You chose Paper, I chose Scissors. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)   
    elif user == 3 and computer == 1:
        var.set("You chose Scissors, I chose Rock. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)    
    elif user == 3 and computer == 2:
        var.set("You chose Scissors, I chose Paper. \nYou win")
        wins.set(wins.get() + 1)
    else:
        var.set("Thanks for playing. \nYou have " + str(win) + " wins and " + str(lose) + " losses.")


    
top = tkinter.Tk()
top.wm_title("RPS Python GUI")
top.minsize(width=280, height=150)
top.maxsize(width=280, height=150)
Button1 = tkinter.Button(top, text ="Rock", command = lambda: game(win, lose, 1))
Button1.grid(row=2, column=1)
Button2 = tkinter.Button(top, text ="Paper", command = lambda: game(win, lose, 2))
Button2.grid(row=2, column=2)
Button3 = tkinter.Button(top, text ="Scissors", command = lambda: game(win, lose, 3))
Button3.grid(row=2, column=5)
space = tkinter.Label(top, text="")
space.grid(row=1)
var = StringVar()
var.set('ROCK PAPER SCISSORS')
l = Label(top, textvariable = var)
l.grid(row=3, column=2)
wins = IntVar()
wins.set(win)
w = Label(top, textvariable = wins)
w.grid(row=5, column=2)
labeled = Label(top, text = "Score:")
labeled.grid(row=4, column=2)
copy = Label(top, text= "Rock Paper Scissors using Python")
copy.grid(row=0, column=2)
top.mainloop()