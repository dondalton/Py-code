import Tkinter, tkFileDialog   # library for open and save file dialogs
from Tkinter import *
import os       # library for changing directory calls
import openpyxl as px     # read xlsx library

# make the home directory the starting point of the open file dialog
from os.path import expanduser
home = expanduser("~")     # get default directory of user
os.chdir(home)
os.chdir("./Documents")     # make ~\documents the starting place
os.chdir('C:/Users/DDalton/Documents/planning/LTE customer data/')

# Open spreadsheet NTUA Tier Throttle
root = Tkinter.Tk()
root.withdraw()
file = tkFileDialog.askopenfilename(title='Throttelz')
try:
    wb = px.load_workbook(file, use_iterators = True)
    # set ws to active workbook, active sheet
    ws = wb.get_sheet_by_name(name = 'RAW')
except:
    print "bad file name"
    exit()

# make directory of first file the new default directory
os.chdir(os.path.dirname(file))

# get saveas filename for output
root = Tkinter.Tk()
root.withdraw()
myFormats = [
    ('csv','*.csv'),
    ]

fileName = tkFileDialog.asksaveasfilename(filetypes=myFormats ,title="Save the output csv file as...")
if ".csv" not in fileName:
    fileName = fileName + ".csv"
if len(fileName ) < 1:
    print "bad file name"
    exit()
try:
    whand = open(fileName,'w')
except:
    print "bad file name"
    exit()

IMSIdict = dict()

lineNo = 0
for row in ws.iter_rows():    # Read the IMTS key customer spreadsheet
    lineNo += 1
    if lineNo > 1:      # skip header
        colNum = 0
        for cell in row:
            if str(cell.value).strip() in IMSIdict:
                IMSIdict[str(cell.value).strip()][colNum] += 1
            else:
                IMSIdict[str(cell.value).strip()]=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                IMSIdict[str(cell.value).strip()][colNum] += 1
            colNum += 1

for key in IMSIdict:
    print key,IMSIdict[key]
        
