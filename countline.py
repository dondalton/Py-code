import Tkinter, tkFileDialog   # library for open and save file dialogs
from Tkinter import *
import os       # library for changing directory calls

# Open spreadsheet
root = Tkinter.Tk()
root.withdraw()
file = tkFileDialog.askopenfilename(title='Open Spreadsheet')
try:
    fhand = open(file)
except:
    print "bad file name"
    exit()

lineNo = 1
for line in fhand:
    lineNo += 1

print "Lines: " + str(lineNo)
