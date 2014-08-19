from Tkinter import *
import tkFileDialog as dialog

def save(root, text):
  data = text.get('0.0', END)
  filename = dialog.asksaveasfilename(
      parent=root,
      filetypes=[('Text', '*.txt')],
      title='Save as...')
  writer = open(filename, 'w')
  writer.write(data)
  writer.close()

def quit(root):
  root.destroy()
  
window = Tk()
text = Text(window)
text.pack()

menubar = Menu(window)
filemenu = Menu(menubar)
filemenu.add_command(label='Save', command=lambda : save(window, text))
filemenu.add_command(label='Quit', command=lambda : quit(window))

menubar.add_cascade(label = 'File', menu=filemenu)
window.config(menu=menubar)

window.mainloop()
