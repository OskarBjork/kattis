from tkinter import *


root = Tk()
root.geometry("300x300")
e = Entry(root)
e.pack()
lbl = Label(root)
lbl.pack()
b = Button(root, text="Hello World")


def click_handler(self):
    lbl["text"] = "Du skrev: " + e.get() + " i rutan"


b.bind("<Button-1>", click_handler)
b.pack()
root.mainloop()
pass
