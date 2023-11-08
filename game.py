from tkinter import *

from record import Record
from myMenu import MyMenu

record = Record()
record.load()

menu = MyMenu()
menu.run()