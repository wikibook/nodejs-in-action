from Tkinter import *

def cross(text):
    text.insert(INSERT, 'X')

window = Tk()
frame = Frame(window)
frame.pack()

text = Text(frame, height=3, width=10)
text.pack()

button = Button(frame, text="Add", command=lambda: cross(text))
button.pack()

window.mainloop()
