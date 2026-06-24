from tkinter import *
from time import strftime

root = Tk()

def update():
    time_string = strftime('%H:%M:%S')
    label.config(text=time_string)
    label.after(1000, update)

label = Label(root, font=('Arial', 50))
label.pack()

update()
root.mainloop()