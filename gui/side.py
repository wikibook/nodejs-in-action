from Tkinter import *
window = Tk()
frame = Frame(window)
frame.pack()
label = Label(frame, text="Name")
label.pack(side="left")
entry = Entry(frame)
entry.pack(side="left")
window.mainloop()
