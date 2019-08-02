from tkinter import *
from tkinter import ttk
from tkinter import font


class Card:
    def __init__(self, root, parent, num, _type):
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        self.title = "Lorem ipsum"
        self.units = "gallons"
        self.color = "black"
        self.bbox = (0, num*(h/5), w, h/5)
        if _type == "forward":
            self.title = "Forward"
            self.units = "meters"
            self.color = "blue"
        elif _type == "back":
            self.title = "Backward"
            self.units = "meters"
            self.color = "red"
        elif _type == "rotate":
            self.title = "Rotate"
            self.units = "degrees"
            self.color = "green"
        else:
            pass

        parent.create_rectangle((0, 0, 0, 0), fill=self.color, highlightbackground='#FFAB8A', tags="card")
        parent.create_text(100, num*(h/8), text=self.title)
        self.amount = ttk.Entry(root)
        parent.create_window(100, num*50, window=self.amount)

    def getCommand(self):
        return f'\t\tself.addSequential({self.title}({self.amount.get()}))\n'
