# Initialization.
from Tkinter import *

# The controller.
def click():
    counter.set(counter.get() + 1)  
    
if __name__ == '__main__':
    # More initialization.
    window = Tk()  
	
    # The model.
    counter = IntVar()
    counter.set(0)
	 
    # The views.
    frame = Frame(window)
    frame.pack()
    
    button = Button(frame, text="Click", command=click)
    button.pack()
    
    label = Label(frame, textvariable=counter)
    label.pack()

    window.mainloop()
