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

distinctIMSI = {}

for line in fhand:
    fields = line.split(",")
    if fields[47] not in distinctIMSI:
        distinctIMSI[fields[47]] = fields[0]

whand.write("Entity,IMSI\n")
for key in distinctIMSI:
    whand.write(key + "," + distinctIMSI[key] + "\n")
    print key + "," + distinctIMSI[key]
whand.close()
