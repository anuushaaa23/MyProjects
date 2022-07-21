import random
import tkinter
from tkinter import *

user = int
computer = int
win = 0             #variable to keep count of wins
lose = 0            #variable to keep count of loses

def rpsls(win, lose, user):             #function for rock paper scissors lizard spock game
    
    computer = random.randrange(1,6)    #Computer's choice
    
    #when user == computer
    if user == computer:
        var.set("It's a draw. \n No Points") 
    
    #user==rock and computer==scissirs   
    elif user == 1 and computer == 3:
        var.set("You chose Rock, I chose Scissors. \nYou win")
        wins.set(wins.get() + 1)
            
    #user==rock and computer==paper
    elif user == 1 and computer == 2:
        var.set("You chose Rock, I chose Paper. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1) 
        
    #user==rock and computer==spock
    elif user == 1 and computer == 4:
        var.set("You chose Rock, I chose Spock. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
        
    #user==rock and computer==lizard
    elif user == 1 and computer == 5:
        var.set("You chose Rock, I chose Lizard. \nYou win")
        wins.set(wins.get() + 1)
        
    #user==Paper and computer==Rock
    elif user == 2 and computer == 1:
        var.set("You chose Paper, I chose Rock. \nYou win")
        wins.set(wins.get() + 1)

    #user==Paper and computer==scissors
    elif user == 2 and computer == 3:
        var.set("You chose Paper, I chose Scissors. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1) 
    
    #user==paper and computer==spock
    elif user == 2 and computer == 4:
        var.set("You chose Paper, I chose Spock. \nYou win")
        wins.set(wins.get() + 1)
        
    #user==paper and computer==lizard
    elif user == 2 and computer == 5:
        var.set("You chose Paper, I chose Lizard. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
        
    #user==scissors and computer==rock
    elif user == 3 and computer == 1:
        var.set("You chose Scissors, I chose Rock. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1) 
    
    #user==scissors and computer==paper
    elif user == 3 and computer == 2:
        var.set("You chose Scissors, I chose Paper. \nYou win")
        wins.set(wins.get() + 1)
    
    #user==scissors and computer==spock
    elif user == 3 and computer == 4:
        var.set("You chose Scissors, I chose Spock. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
        
    #user==scissors and computer==lizard
    elif user == 3 and computer == 5:
        var.set("You chose Scissors, I chose Lizard. \nYou win")
        wins.set(wins.get() + 1)
    
    #user==spock and computer==rock
    elif user == 4 and computer == 1:
        var.set("You chose Spock, I chose Rock. \nYou win")
        wins.set(wins.get() + 1)
    
    #user==spock and computer==paper
    elif user == 4 and computer == 2:
        var.set("You chose Spock, I chose Paper. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
    
    #user==spock and computer==scissors
    elif user == 4 and computer == 3:
        var.set("You chose Spock, I chose Scissors. \nYou win")
        wins.set(wins.get() + 1)
    
    #user==spock and computer==lizard
    elif user == 4 and computer == 5:
        var.set("You chose Spock, I chose Lizard. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
    
    #user==lizard and computer==rock
    elif user == 5 and computer == 1:
        var.set("You chose Lizard, I chose Rock. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
    
    #user==lizard and computer==paper
    elif user == 5 and computer == 2:
        var.set("You chose Lizard, I chose Paper. \nYou win")
        wins.set(wins.get() + 1)
    
    #user==lizard and computer==scissors
    elif user == 5 and computer == 3:
        var.set("You chose Lizard, I chose Scissors. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
    
    #user==lizard and computer==spock
    elif user == 5 and computer == 4:
        var.set("You chose Lizard, I chose Spock. \nYou win")
        wins.set(wins.get() + 1)
 
    else:
        var.set("Thanks for playing. \nYou have " + str(win) + " wins and " + str(lose) + " losses.")


# using tkinter to create a GUI for the game    
top = tkinter.Tk() 
top.wm_title("RPSLS GUI")
top.minsize(width=385, height=150)
top.maxsize(width=385, height=150)
top.configure(bg="azure3")

#Rock button
B1 = tkinter.Button(top, text ="ROCK", command = lambda: rpsls(win, lose, 1),fg="black",bg="gainsboro")       
B1.grid(row=0, column=1)

 #Paper button
B2 = tkinter.Button(top, text ="PAPER", command = lambda: rpsls(win, lose, 2),fg="black",bg="gainsboro")     
B2.grid(row=0, column=2)

#Scissors button
B3 = tkinter.Button(top, text ="SCISSORS", command = lambda: rpsls(win, lose, 3),fg="black",bg="gainsboro")   
B3.grid(row=0, column=3)

#Spock button
B4 = tkinter.Button(top, text ="SPOCK", command = lambda: rpsls(win, lose, 4),fg="black",bg="gainsboro")      
B4.grid(row=0, column=4)

#Lizard button
B5 = tkinter.Button(top, text ="LIZARD", command = lambda: rpsls(win, lose, 5),fg="black",bg="gainsboro")     
B5.grid(row=0, column=5)

space = tkinter.Label(top, text="",bg="azure3")
space.grid(row=1)

var = StringVar()
var.set('Welcome!')
l = Label(top, textvariable = var,bg="azure3") #displaying the status of the game
l.grid(row=2, column=3)

wins = IntVar()
wins.set(win)
w = Label(top, textvariable = wins,bg="azure3") #displaying the score
w.grid(row=4, column=3)

labeled = Label(top, text = "Score:",bg="azure3")
labeled.grid(row=3, column=3)

copy = Label(top, text= "      RPSLS game using python      ",bg="azure3")
copy.grid(row=5, column=3)

top.mainloop()