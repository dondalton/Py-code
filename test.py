import Tkinter, tkFileDialog   # library for open and save file dialogs
from Tkinter import *
import os       # library for changing directory calls

#  concats all files in the same directory as the output file!!!!!

# get saveas filename for output
root = Tkinter.Tk()
root.withdraw()

outfileName = tkFileDialog.asksaveasfilename(title="Save the output file as...")
if len(outfileName ) < 1:
    print "bad file name"
    exit()

# make directory of first file the new default directory
os.chdir(os.path.dirname(outfileName))
path = os.path.dirname(outfileName)
print path
print
print
for files in os.listdir(path):
    print files

 
