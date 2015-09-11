from Tkinter import *
import Tkinter
from tkMessageBox import *

def answer():
    showerror("Answer", "Sorry, no answer available")

def callback():
    if askyesno('Verify', 'Really quit?'):
        showwarning('Yes', 'Not yet implemented')
        root.withdraw()
        exit()
    else:
        showinfo('No', 'Quit has been cancelled')
        
root = Tkinter.Tk()
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Answer', command=answer).pack(fill=X)
mainloop()
