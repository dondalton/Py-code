import Tkinter, tkFileDialog   # library for open and save file dialogs
from Tkinter import *
import os       # library for changing directory calls

# Open spreadsheet
root = Tkinter.Tk()
root.withdraw()
file = tkFileDialog.askopenfilename(title='Open file1')
try:
    fhand1 = open(file)
except:
    print "bad file name"
    exit()

# make directory of first file the new default directory
os.chdir(os.path.dirname(file))

# Open file
root = Tkinter.Tk()
root.withdraw()
file = tkFileDialog.askopenfilename(title='Open file2')
try:
    fhand2 = open(file)
except:
    print "bad file name"
    exit()

    # get saveas filename for output
root = Tkinter.Tk()
root.withdraw()

fileName = tkFileDialog.asksaveasfilename(title="Save the output file as...")
if len(fileName ) < 1:
    print "bad file name"
    exit()
try:
    whand = open(fileName,'w')
except:
    print "bad file name"
    exit()

for line in fhand1:
    whand.write(line)

for line in fhand2:
    whand.write(line)
whand.close()
