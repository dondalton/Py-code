import Tkinter, tkFileDialog   # library for open and save file dialogs
from Tkinter import *
import os       # library for changing directory calls

# Open spreadsheet
from os.path import expanduser
home = expanduser("~")     # get default directory of user
os.chdir(home)
os.chdir("./Documents")
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
whand.write("select sum(DataVolumeFBCDownlink), substring(RecordOpeningTime,12,2), ServedIMSI from April where ")
for line in fhand:
    whand.write("\"" + line.strip() + "\" = ServedIMSI or ")

whand.close()
