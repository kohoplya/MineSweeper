from tkinter import *
from random import shuffle
from tkinter import messagebox

from button import MyButton
from record import Record

class MineSweeper:

    ROW = 10
    COLUMNS = 15
    MINES = int((ROW * COLUMNS) * 16 / 100) + 1
    print(MINES)
    IS_GAME_OVER = False
    zero = 0
    currentOpened = 0

    def __init__(self):
        self.buttons = []
        count = 1
        self.window = Tk()
        self.window.resizable(width=False, height=False)
        self.window.title("MineSweeper")

        for i in range (MineSweeper.ROW):
            temp = []
            for j in range (MineSweeper.COLUMNS):
                btn = MyButton(self.window, x = i, y = j, number = count, field = self)
                btn.config(command= lambda button = btn: self.click(button))
                temp.append(btn)
                count += 1
            self.buttons.append(temp)

    def closing(self):
        record = Record()
        record.save(self.currentOpened)

        if messagebox.askokcancel("closing", "Close the application and exit to the main menu"):
            self.window.destroy()
            from myMenu import MyMenu

            menu = MyMenu()
            menu.run()

    def click(self, currentButton: MyButton):
        if self.IS_GAME_OVER == True:
            return
        
        if currentButton.isMine:
            currentButton.config(text= '*', background= 'red', disabledforeground='black')
            self.IS_GAME_OVER = True
            messagebox.showinfo('GAME OVER', ' YOU LOOSE')

            for i in range (MineSweeper.ROW):
                for j in range (MineSweeper.COLUMNS):
                    btn = self.buttons[i][j]
                    if btn.isMine:
                        btn.config(text = '*', background= 'red')

            self.window.protocol("WM_DELETE_WINDOW", self.closing)

        elif currentButton.minesCount == 0:
            self.openEmpty(currentButton)
        else:
            currentButton.config(text= currentButton.minesCount)
            self.currentOpened += 1

        currentButton.config(state= 'disabled')

    def createWidgets(self):
        for i in range (MineSweeper.ROW):
            for j in range (MineSweeper.COLUMNS):
                btn = self.buttons[i][j]
                btn.grid(row = i, column = j)


    def start(self):
        self.createWidgets()
        self.createMines()
        self.printButtons()

        for row in self.buttons:
            for btn in row:
                btn.checkNeighbors(self.buttons)
                if btn.minesCount == 0 and btn.isMine == False and self.zero == 0 and btn.x > 0:
                    btn.config(background = 'green')
                    self.zero = 1
    
    def printButtons(self):
        for row in self.buttons:
            print(row)

    def getMinesCord(self):
        indexes = list(range(1, self.COLUMNS * self.ROW + 1))
        shuffle(indexes)
        return indexes[:self.MINES]
    
    def createMines(self):
        minesIndex = self.getMinesCord()
        print(minesIndex)
        for row in self.buttons:
            for btn in row:
                if btn.number in minesIndex:
                    btn.isMine = True

    def checkMines(self):
        currentMines = 0

        for i in range (self.ROW):
            for j in range (self.COLUMNS):
                btn = self.buttons[i][j]

                if btn.isMine == True and btn.cget("text") == '*':
                    currentMines +=1

        if currentMines == self.MINES:
            return True

    def openEmpty(self, currentButton: MyButton):
        currentButton.config(text='', relief = SUNKEN, state='disabled')

        queue = [(currentButton.x, currentButton.y)]
        visited = set()

        while queue:
            x, y = queue.pop(0)


            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_x = x + i
                    new_y = y + j

                    if 0 <= new_x < MineSweeper.ROW and 0 <= new_y < MineSweeper.COLUMNS:
                        neighbor = self.buttons[new_x][new_y]
                        if (neighbor.minesCount == 0 and not neighbor.isMine) and (new_x, new_y) not in visited:
                            neighbor.config(text='', relief = SUNKEN, background = '#cfcfcf', state='disabled')

                            queue.append((new_x, new_y))
                            visited.add((new_x, new_y))
                        elif neighbor.minesCount > 0:
                            neighbor.config(text=neighbor.minesCount, state='disabled')

