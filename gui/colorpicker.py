from Tkinter import *
def change(widget, colors):
    '''Update the foreground color of a widget to show the RGB color value
    stored in a dictionary with keys 'red', 'green', and 'blue'.  Does
    *not* check the color value.
    '''
    new_val = '#'
    for name in ('red', 'green', 'blue'):
        new_val += colors[name].get()
    widget['bg'] = new_val
# Create the application.
window = Tk()
frame = Frame(window)
frame.pack()
# Set up text entry widgets for red, green, and blue, storing the
# associated variables in a dictionary for later use.
colors = {}
for (name, col) in (('red', '#FF0000'),
                    ('green', '#00FF00'),
                    ('blue', '#0000FF')):
    colors[name] = StringVar()
    colors[name].set('00')
    entry = Entry(frame, textvariable=colors[name], bg=col, fg="white")
    entry.pack()
# Display the current color.
current = Label(frame, text='     ', bg='#FFFFFF')
current.pack()
# Give the user a way to trigger a color update.
update = Button(frame, text='Update', command=lambda: change(current, colors))
update.pack()
# Run the application.
mainloop()
