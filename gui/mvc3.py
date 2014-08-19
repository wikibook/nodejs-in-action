# Initialization.
from Tkinter import *
window = Tk()

# The model.
counter = IntVar()
counter.set(0)

# General controller
def click(var, value):
    var.set(var.get() + value)

# The views.
frame = Frame(window)
frame.pack()

button = Button(frame, text="Up", command=lambda: click(counter, 1))
button.pack()

button = Button(frame, text="Down", command=lambda: click(counter, -1))
button.pack()

label = Label(frame, textvariable=counter)
label.pack()

window.mainloop()
