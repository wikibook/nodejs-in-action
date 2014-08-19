from Tkinter import *

window = Tk()
frame = Frame(window)
frame.pack()
red = IntVar()
green = IntVar()
blue = IntVar()

for (name, var) in (('R', red), ('G', green), ('B', blue)):
    check = Checkbutton(frame, text=name, variable=var)
    check.pack(side='left')
def recolor(widget, r, g, b):
    color = '#'
    for var in (r, g, b):
        color += 'FF' if var.get() else '00'
    widget.config(bg=color)
	
label = Label(frame, text='[       ]')
button = Button(frame, text='update',
                command=lambda: recolor(label, red, green, blue))
button.pack(side='left')
label.pack(side='left')
window.mainloop()
