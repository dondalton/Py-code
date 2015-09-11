import Tkinter, tkFileDialog   # library for open and save file dialogs
from Tkinter import *
import os       # library for changing directory calls

os.chdir("c:/users/ddalton/documents")

# Open spreadsheet
root = Tkinter.Tk()
root.withdraw()
file = tkFileDialog.askopenfilename(title='Open Spreadsheet')
try:
    fhand = open(file)
except:
    print "bad file name"
    exit()

distinctsectsig = {}
distinctaccsig = {}

for line in fhand:
    if "QuickConfig" in line:
        for i in (1,5):
            line = next(fhand)
        if "Sector ID" in line:
            sectID = line.split()[3]
            line = next(fhand)
            sectsig = line.split()[3]
            line = next(fhand)
            accsig = line.split()[3]
            if sectID not in distinctsectsig:
                distinctsectsig[sectID] = sectsig
                distinctaccsig[sectID] = accsig
            #print sectID + "  " + sectsig + "  " + accsig

for key in distinctsectsig:
    print key + "  " + distinctsectsig[key] + "  " + distinctaccsig[key]
