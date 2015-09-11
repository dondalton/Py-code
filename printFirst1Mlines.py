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

# make directory of first file the new default directory
os.chdir(os.path.dirname(file))

    # get saveas filename for output
root = Tkinter.Tk()
root.withdraw()
myFormats = [
    ('text','*.txt'),
    ]

fileName = tkFileDialog.asksaveasfilename(filetypes=myFormats ,title="Save the output text file as...")
if len(fileName ) < 1:
    print "bad file name"
    exit()
try:
    whand = open(fileName,'w')
except:
    print "bad file name"
    exit()

lineNo = 1
for line in fhand:
    field = list(line.split(","))
    #print field[2],field[11], field[12],field[15],field[17],field[20],field[38],field[45],field[46]
    if lineNo > 1:
        whand.write(field[2] + "," + field[11] + "," + field[12] + "," + field[15] + "," + field[17] + "," + field[20] + "," + field[38] + "," + field[45] + "," + field[46] + "\n")
    lineNo += 1
    if lineNo > 1000000:
        break
whand.close()
