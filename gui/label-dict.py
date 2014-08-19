from Tkinter import *
import time

window = Tk()
label = Label(window, text="First label.")
label.pack()
time.sleep(2)
label.config(text="Second label.")