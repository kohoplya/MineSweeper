from tkinter import *

from mineSweeper import MineSweeper
from record import Record

class MyMenu():
    def __init__(self):
        self.record = Record()
        self.record.load()

        self.mainWindow = Tk()
        self.mainWindow.geometry("400x300")
        self.mainWindow.resizable(width= False, height= False)
        self.mainWindow.title("MENU")

        menuText = Label(self.mainWindow, text= "MAIN MENU", font='Calibri 17 bold')
        menuText.place(x = 150, y = 25)

        btnStart = Button(self.mainWindow, text="Start game", width= 35, height= 2, bd=2, fg = 'black', bg = 'grey', font='Calibri 11 bold', command= self.startGame)
        btnStart.place(x = 65, y = 90)

        btnStart = Button(self.mainWindow, text="EXIT", width= 35, height= 2, bd=2, fg = 'black', bg = 'red', font='Calibri 11 bold', command= self.mainWindow.destroy)
        btnStart.place(x = 65, y = 150)

        recordText = Label(self.mainWindow, text= f"Record: {self.record.maxOpened}", font='Calibri 15 bold')
        recordText.place(x = 65, y = 220)

    def startGame(self):
        self.mainWindow.destroy()
        game = MineSweeper()
        game.start()


    def run(self):
        self.mainWindow.mainloop()