from Tkinter import *
window = Tk()
frame = Frame(window)
frame.pack()
label = Label(frame, text="Name:")
label.grid(row=0, column=0)
entry = Entry(frame)
entry.grid(row=1, column=1)
window.mainloop()
