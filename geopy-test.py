import geopy
from geopy.distance import vincenty

import os       # library for changing directory calls
import Tkinter, tkFileDialog   # library for open and save file dialogs
from Tkinter import *
import openpyxl as px     # read xlsx library

# make the home directory the starting point of the open file dialog
from os.path import expanduser
home = expanduser("~")     # get default directory of user
os.chdir(home)
os.chdir("./Documents")
os.chdir('C:\Users\DDalton\Documents\RF performance\site list')

# Open spreadsheet
root = Tkinter.Tk()
root.withdraw()
file = tkFileDialog.askopenfilename(title='Google spreadsheet')
try:
    #read workbook
    wb = px.load_workbook(file, use_iterators = True)
    # set ws to active workbook, active sheet
    ws = wb.get_sheet_by_name(name = 'Google_Location_Services_Commne')
    #ws = wb.active
except:
    print "error opening file"
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

lineno = 1
lat2 = "latitude"
lon2 = "longitude"

for row in ws.iter_rows():
    if lineno > 1:
        lat1 = float(row[6].value)
        lon1 = float(row[7].value)
        origin = geopy.point.Point(lat1, lon1)
        print origin
        d = 15
        b = row[9].value
        destination = geopy.distance.vincenty(kilometers=d).destination(origin, b)
        lat2 = destination.latitude
        lon2 = destination.longitude
        print lat2, lon2
    whand.write(str(row[0].value) + "," + str(row[1].value) + "," + str(row[2].value) + "," + str(row[3].value) + "," + str(row[4].value) + "," + str(row[5].value) + "," + str(row[6].value) + "," + str(row[7].value) + "," + str(row[8].value) + "," + str(row[9].value) + "," + str(row[10].value) + "," + str(row[11].value) + "," + str(lat2) + "," + str(lon2) + "," + str(row[14].value) + "\n")
    lineno += 1

whand.close()
