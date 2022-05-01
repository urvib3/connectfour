# CONNECT FOUR
# apcsp 2022 digital portfolio
# IMPORTS
import tkinter as tk
from tkinter import *
# SET UP
app = tk.Tk()
app.geometry("400x400")
app['background'] = 'black'
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_columnconfigure(0, weight=1)
boardFrame = Frame(app)
boardFrame.grid(row=1, column=0)
# VARIABLES
nextSpot = [0 for i in range (7)]
number of the next empty spot in the row where 0 is the most bottom
spot
# images for cells screenshotted from https://currenthomeny.com/
products/four-in-a-row-white-blue
empty = PhotoImage(file = "empty.png")
dark = PhotoImage(file = "darkblue.png")
light = PhotoImage(file = "lightblue.png")
player = 1
player is light blue; 1 = light blue; 2 = dark blue
# initial
1 = light blue
# CELL CLASS (DATA TYPE)
class Cell(Button):
    status = 0
2 = dark blue
    row = 0
column = 0
# 0 = no player occupied
def __init__ (self, row, col):
    self.row = row
    self.column = col
# row
        super().__init__(boardFrame, command=lambda: move(col),
image=empty, bd=0, highlightthickness=0, width=85, height=85)
        super().grid(row=4-row, column=col,  sticky="nsew")
     def switchPlayer(self, player):
to inputted player (1 or 2)
        self.status = player
        if self.status == 1:
            super().config(image=light)
        if self.status == 2:
            super().config(image=dark)
    def disable(self):
clicking cells and making moves after game is won
        super().config(state=DISABLED)
    def reset(self):
for a new game
        super().config(image=empty)
        super().config(state=ACTIVE)
        self.status = 0
board = [[" " for x in range(7)] for y in range(5)]
of all the buttons comprising the visual board (COLLECTION)
# CREATE ALL BOARD CELLS AND STORE THEM IN BOARD ARRAY (COLLECTION
INITIALIZIATION)
for row in range(5):
    for col in range(7):
        board[row][col] = Cell(row, col)
# HELPER FUNCTIONS
# called every time a cell is clicked to place a chip
# col = column of the button clicked
def move(col):
    row = nextSpot[col]
    if (row < 5):
has space for another chip
        board[row][col].switchPlayer(player)
status at corresponding cell; switchPlayer() will also change image of
cell accordingly
        nextSpot[col] += 1                      # updates nextSpot so
that next empty spot in column is one cell higher up
        message.config(text=("GAME IN PROGRESS"))
        checkwin(row, col)
chip results in a player winning
        switchPlayer()
# checks if new
  # switches
player
# switches cell's status
# prevents user from
# called in reset function
# confirms that column
# changes player
# 2d array

    else :
        message.config(text=("INVALID MOVE"))
def switchPlayer():
    global player
    if (player == 1):
        player = 2
    else:
        player = 1
def declarewin(): # HELPER FUNCTION FOR CHECKWIN()
    if player == 1:   message.config(text=("LIGHT BLUE WINS!"))
    if player == 2:   message.config(text=("DARK BLUE WINS"))
    disable()
def checkwin(row, col):
    # VERTICAL WINS
    cchips = 1           # consecutive chips
    crow = row
    while (crow >= 1 and board[crow-1][col].status == player):
crow -= 1
        cchips += 1
    crow = row
    while (crow <= 3 and board[crow+1][col].status == player):
        crow += 1
        cchips += 1
    if (cchips >= 4): declarewin()
    # HORIZONTAL WINS
    cchips = 1
    ccol = col
    while (ccol >= 1 and board[row][ccol-1].status == player):
ccol -= 1
        cchips += 1
    ccol = col
    while (ccol <= 5 and board[row][ccol+1].status == player):
        ccol += 1
        cchips += 1
    if (cchips >= 4): declarewin()
    # UPWARD DIAGONAL WINS
    cchips = 1
    crow = row
    ccol = col
    while (ccol >= 1 and crow >= 1 and board[crow-1][ccol-1].status ==
player):
        ccol -= 1
        crow -= 1
        cchips += 1
ccol = col
 
crow = row
    while (ccol <= 5 and crow <= 3 and board[crow+1][ccol+1].status ==
player):
        ccol += 1
        crow += 1
        cchips += 1
    if (cchips >= 4): declarewin()
    # DOWNARD DIAGONAL WINS
    cchips = 1
    crow = row
    ccol = col
    while (ccol >= 1 and crow <= 3 and board[crow+1][ccol-1].status ==
player):
        ccol -= 1
        crow += 1
        cchips += 1
        print ("row: " + str(row) + " column: " + str(col) + " crow: "
+ str(crow) + " ccolumn: " + str(ccol) + " cchips: "  + str(cchips) +
"in left to right downward diagonal")
    ccol = col
    crow = row
    while (ccol <= 5 and crow >= 1 and board[crow-1][ccol+1].status ==
player):
        ccol += 1
crow -= 1
        cchips += 1
    if (cchips >= 4): declarewin()
def disable():          # disable all buttons once player has won
    for i in range(5):
         for j in range(7):
            board[i][j].disable()
def reset():
    for row in range(5):
        for col in range(7):
            board[row][col].reset()
statuses to no player
    for i in range(7):
        nextSpot[i] = 0
    message.config(text="GAME IN PROGRESS")  # reset game status
# SIDE FRAMES
titleFrame = Frame(app)
titleFrame.grid(row=0, column=0)
title = Label(titleFrame, text="CONNECT FOUR", font=("Impact", 50),
# reset all cell
# reset least empty spot

bg="black", fg="white")
title.grid(row=0, column=0)
messageFrame = Frame(app, bg='black')
messageFrame.grid(row=2, column=0)
message = Label(messageFrame, text="GAME IN PROGRESS", font=("Comic
Sans MS", 32), bg="black", fg="white")
# reset button image taken from https://www.istockphoto.com/
illustrations/reset-button
resetImage = PhotoImage(file = "resetbutton.png")
resetButton = tk.Button(messageFrame, image = resetImage, bd=0,  width
= 150, height = 70, command=reset)
placeholder = Label(messageFrame, height=1, bg="black")
message.grid(row=0, column=0)
placeholder.grid(row=1, column=0)
resetButton.grid(row=2, column=0, sticky="s")
app.mainloop()
