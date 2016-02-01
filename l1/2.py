__author__ = 'vonking'

from Tkinter import *


def change_relief():
    reliefList = ['flat', 'raised', 'sunken', 'groove', 'ridge']
    global reliefIndex
    label.config(relief=reliefList[reliefIndex % len(reliefList)])
    reliefIndex += 1


def change_color(event):
    colorList = ['red', 'green', 'blue', 'yellow']
    global colorIndex
    label.config(fg=colorList[colorIndex % len(colorList)])
    colorIndex += 1

reliefIndex = 0
colorIndex = 0

root = Tk()

label = Label(root, text='Welcome to Python!')
#canvas = Canvas(root, bg="white")
button1 = Button(root, text='relief!', command=change_relief)
button2 = Button(root, text='color!')
button2.bind("<Button-1>", change_color)

label.pack()
#canvas.pack()
button1.pack(side=LEFT, anchor=CENTER, expand=YES)
button2.pack(side=LEFT, anchor=CENTER, expand=YES)

root.mainloop()