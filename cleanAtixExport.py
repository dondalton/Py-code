import os       # library for changing directory calls
import Tkinter, tkFileDialog   # library for open and save file dialogs
from Tkinter import *

from os.path import expanduser
home = expanduser("~")     # get default directory of user
os.chdir(home)
os.chdir("./Documents")
os.chdir("C:/Users/DDalton/Documents/planning/mobility fund/All Steve drives")

root = Tkinter.Tk()
root.withdraw()
file = tkFileDialog.askopenfilename(title='Actix export file directory')

# make directory of first file the new default directory
os.chdir(os.path.dirname(file))

#loop through all files in dir
path = os.path.dirname(file)
for files in os.listdir(path):
    #only .txt files
    if os.path.splitext(files)[1] == ".txt":
        print files

        try:
            fhand = open(files)
        except:
            print "bad file name"
            exit()
        
        myFormats = [
            ('text','*.txt'),
            ]

        fileName = os.path.splitext(files)[0]
        fileName = fileName + ".csv"
        print fileName

        # open output file as same name, but .csv extension
        try:
            whand = open(fileName,'w')
        except:
            print "bad file name"
            exit()

        for line in fhand:
            fields = line.split(",")
            if len(fields) > 3:
                if len(fields[1]) > 1 and len(fields[2]) > 1 and len(fields[3]) > 1:
                    #print fields[1].translate(None,'"') + "," + fields[2].translate(None,'"') + "," + fields[3].translate(None,'"' + "\n")
                    whand.write(fields[1].translate(None,'"') + "," + fields[2].translate(None,'"') + "," + fields[3].translate(None,'"'))
            
whand.close()
