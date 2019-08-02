from tkinter import *
from tkinter import ttk
from tkinter import font
import os
from card import Card


# Grid is three by six
# ----------------------
# |    |    |     |     |
# |    |    |     |     |
# |    |    |     |     |
# |    |    |     |     |
# |    |____|_____|     |
# |    |    |     |     |
# -----------------------
cards = []


def deploy():
    # os.system("python3 code/robot.py test")
    f = open(os.getcwd() + "/code/commands/autonomous.py", "a")
    for card in cards:
        f.write(card.getCommand())
    f.close()
    print("DEPLOYED")


def write_speed():
    cards.append(Card(root, l_canvas, len(cards), "rotate"))


def write_rotate():
    cards.append(Card(root, l_canvas, len(cards), "rotate"))


def write_forward():
    cards.append(Card(root, l_canvas, len(cards), "forward"))


def write_backward():
    cards.append(Card(root, l_canvas, len(cards), "back"))


with open(os.getcwd() + "/code/commands/drivedistance.py", "r") as content_file:
    contents = content_file.read()
root = Tk()
root.title("Autonomous App")
open_sans_bold = font.Font(family="Open Sans Semibold", size=36)

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
ttk.Style().configure("Left.TLabel", foreground="white", background="#687AFF")
ttk.Style().configure("Right.TLabel", foreground="white", background="#FF8E87")
ttk.Style().configure("Left.TFrame", background="#687AFF")
ttk.Style().configure("Right.TFrame", background="#FF8E87")

mainframe = ttk.Frame(root, padding="3 3 12 12", width=w, height=h)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


left = ttk.Frame(mainframe, width=w/2, height=h, style="Left.TFrame")
left.grid(column=0, row=0, columnspan=3, rowspan=3)
l_label = ttk.Label(left, text="Cards",
                    style="Left.TLabel", font=open_sans_bold)
l_label.place(x=w/50, y=h/50)

l_canvas = Canvas(left, width=(w/2.25), height=(h * 0.75))
l_canvas.place(x=w/50, y=w/16)
l_canvas.configure(background="white")

l_button = Button(left, text="Deploy Code", width=20, height=0, highlightbackground='#3E4149', command=deploy, relief=FLAT)
l_button.place(anchor=NW, x=w/50, y=h*0.75)

l_button1 = Button(left, text="Go Forward", width=10, height=0, highlightbackground='#3E4149', command=write_forward, relief=FLAT)
l_button1.place(anchor=NW, x=150, y=800)
l_button2 = Button(left, text="Rotate", width=10, height=0, highlightbackground='#3E4149', command=write_rotate, relief=FLAT)
l_button2.place(anchor=NW, x=50, y=800)
l_button3 = Button(left, text="Go Backward", width=10, height=0, highlightbackground='#3E4149', command=write_backward, relief=FLAT)
l_button3.place(anchor=NW, x=250, y=800)

right = ttk.Frame(mainframe, width=w/2, height=h, style="Right.TFrame")
right.grid(column=3, row=0, columnspan=3, rowspan=3)
r_label = ttk.Label(right, text="Code",
                    style="Right.TLabel", font=open_sans_bold)
r_label.place(x=1+(w/50), y=1+(h/50))

r_canvas = Canvas(right, width=(w/2.25), height=(h * 0.82))

# Add font, and fix colors for everything
r_canvas.create_text(15, 10, fill="darkblue",
                     font="Times 20 italic bold", text=contents, anchor=NW)
r_canvas.place(x=1+(w/50), y=1+(w/16))
r_canvas.configure(background="white")

root.mainloop()
