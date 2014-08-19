from Tkinter import *

class Counter:
    '''A simple counter GUI using object-oriented programming.'''
    def __init__(self, parent):
        '''Create the GUI.'''
        # Framework.
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()

        # Model.
        self.state = IntVar()
        self.state.set(1)

        # Label displaying current state.
        self.label = Label(self.frame, textvariable=self.state)
        self.label.pack()

        # Buttons to control application.
        self.up = Button(self.frame, text='up', command=self.upClick)
        self.up.pack(side='left')

        self.right = Button(self.frame, text='quit', command=self.quitClick)
        self.right.pack(side='left')

    def upClick(self):
        '''Handle click on 'up' button.'''
        self.state.set(self.state.get() + 1)

    def quitClick(self):
        '''Handle click on 'quit' button.'''
        self.parent.destroy()

if __name__ == '__main__':
    window = Tk()
    myapp = Counter(window)
    window.mainloop()
