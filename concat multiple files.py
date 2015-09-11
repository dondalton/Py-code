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
try:
    whand = open(outfileName,'w')
except:
    print "bad file name"
    exit()

# make directory of first file the new default directory
os.chdir(os.path.dirname(outfileName))

for (dirname, dirs, files) in os.walk(os.path.dirname(outfileName)):
    for filename in files:
        if filename != os.path.basename(outfileName):
            print filename + "      " + os.path.basename(outfileName)
            filenameFull = os.path.join(dirname,filename)
            print filenameFull
            try:
                fhand = open(filenameFull)
            except:
                print "bad file name: " + filenameFull
            for line in fhand:
                whand.write(line)

whand.close()
