from tkinter import *
from tkinter import messagebox

class MyButton(Button):
    def __init__(self, master, x, y, number, field, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font='Calibri 15 bold',  *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.field = field
        self.minesCount = 0
        self.isMine = False
        self.bind("<Button-3>", self.rightClick)

    def __repr__(self):
        return f"Button {self.x}, {self.y}, {self.number}, {self.isMine}"
    
    def checkNeighbors(self, buttons):
        from mineSweeper import MineSweeper

        minesCount = 0

        x = self.x
        y = self.y

        if x > 0 and y > 0 and buttons[x - 1][y - 1].isMine:
            minesCount += 1

        if x > 0 and buttons[x - 1][y].isMine:
            minesCount += 1

        if x > 0 and y < MineSweeper.COLUMNS - 1 and buttons[x - 1][y + 1].isMine:
            minesCount += 1

        if y > 0 and buttons[x][y - 1].isMine:
            minesCount += 1

        if y < MineSweeper.COLUMNS - 1 and buttons[x][y + 1].isMine:
            minesCount += 1

        if x < MineSweeper.ROW - 1 and y > 0 and buttons[x + 1][y - 1].isMine:
            minesCount += 1

        if x < MineSweeper.ROW - 1 and buttons[x + 1][y].isMine:
            minesCount += 1

        if x < MineSweeper.ROW - 1 and y < MineSweeper.COLUMNS - 1 and buttons[x + 1][y + 1].isMine:
            minesCount += 1

        self.minesCount = minesCount

        if self.minesCount == 1:
            self.config(disabledforeground='blue')
        elif self.minesCount == 2:
            self.config(disabledforeground='green')
        elif self.minesCount == 3:
            self.config(disabledforeground='red')
        elif self.minesCount == 4:
            self.config(disabledforeground='dark blue')
        elif self.minesCount == 5:
            self.config(disabledforeground='dark red')
        else:
            self.config(disabledforeground='light blue')


    def rightClick(self, event):
        if self.cget("state") != 'disabled':
            if self.cget("text") == '*':
                self.config(text='')
            else:
                self.config(text='*')
                if self.field.checkMines() == True:
                    messagebox.showinfo('win', ' YOU WON!')
                    self.field.closing()

