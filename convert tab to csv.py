import os       # library for changing directory calls
import Tkinter, tkFileDialog   # library for open and save file dialogs
from Tkinter import *

from os.path import expanduser
home = expanduser("~")     # get default directory of user
os.chdir(home)
os.chdir("./Documents")
#os.chdir("C:\Users\DDalton\Documents\planning\mobility fund\ATNI_RAW_DATA_08062015\RAW_DATA_MEREGED")

root = Tkinter.Tk()
root.withdraw()
file = tkFileDialog.askopenfilename(title='scanner data file')
try:
    fhand = open(file)
except:
    print "bad file name"
    exit()

# make directory of first file the new default directory
os.chdir(os.path.dirname(file))

fileName = os.path.splitext(file)[0]
fileName = fileName + ".csv"
print fileName

# open output file as same name, but .csv extension
try:
    whand = open(fileName,'w')
except:
    print "bad file name"
    exit()

for line in fhand:
        whand.write(line.replace('\t',','))
        
whand.close()
