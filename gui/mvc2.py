# Initialization.
from Tkinter import *
window = Tk()
# The model.
counter = IntVar()
counter.set(0)

# Two controllers
def click_up():
    counter.set(counter.get() + 1)
def click_down():
    counter.set(counter.get() - 1)

# The views.
frame = Frame(window)
frame.pack()
button = Button(frame, text="Up", command=click_up)
button.pack()
button = Button(frame, text="Down", command=click_down)
button.pack()
label = Label(frame, textvariable=counter)
label.pack()
window.mainloop()