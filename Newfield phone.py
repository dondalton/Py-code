import os       # library for changing directory calls
import Tkinter, tkFileDialog   # library for open and save file dialogs
from Tkinter import *

from os.path import expanduser
home = expanduser("~")     # get default directory of user
os.chdir(home)
os.chdir("./Documents")
os.chdir("C:\Users\DDalton\Documents\planning\mobility fund\ATNI_RAW_DATA_08062015\RAW_DATA_MEREGED")

root = Tkinter.Tk()
root.withdraw()
file = tkFileDialog.askopenfilename(title='phone data file')
try:
    fhand = open(file)
except:
    print "bad file name"
    exit()

# make directory of first file the new default directory
os.chdir(os.path.dirname(file))

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

i=0

for line in fhand:
    if i==0:
        i=i + 1
        whand.write("Latitude, Longitude, Running tput" + "\n")
    else:
        
        fields = line.split("\t")
        whand.write(fields[1].translate(None,'"') + "," + fields[2].translate(None,'"') + "," + fields[8].translate(None,'"') + "\n")
        
whand.close()
