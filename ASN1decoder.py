import Tkinter, tkFileDialog   # library for open and save file dialogs
from Tkinter import *
import os       # library for changing directory calls
from pyasn1_modules import pem
from pyasn1.codec.ber import decoder
from pyasn1 import debug

# Open spreadsheet
root = Tkinter.Tk()
root.withdraw()
file = tkFileDialog.askopenfilename(title='Open ASN.1 file')
try:
    fhand = open(file)
except:
    print "bad file name"
    exit()

### make directory of first file the new default directory
##os.chdir(os.path.dirname(file))
##
##    # get saveas filename for output
##root = Tkinter.Tk()
##root.withdraw()
##myFormats = [
##    ('text','*.txt'),
##    ]
##
##fileName = tkFileDialog.asksaveasfilename(filetypes=myFormats ,title="Save the output text file as...")
##if len(fileName ) < 1:
##    print "bad file name"
##    exit()
##try:
##    whand = open(fileName,'w')
##except:
##    print "bad file name"
##    exit()

debug.setLogger(debug.Debug('all'))
decoder.decode.defaultErrorState = decoder.stDumpRawValue
substrate = pem.readPemFromFile(open(file))
decoder.decode(substrate)
