import os       # library for changing directory calls
import Tkinter, tkFileDialog   # library for open and save file dialogs
import openpyxl as px     # read xlsx library
import re

# make the home directory the starting point of the open file dialog
from os.path import expanduser
home = expanduser("~")     # get default directory of user
##os.chdir(home)
##os.chdir("./Documents")
os.chdir('C:\Users\DDalton\Documents\RF design\ATT Northern AZ overlay\spectrum map')

# open tab delimeted file with spectrum holdings:
# Radio Service Desc	County	State	FIPS Code	Total BW	Call Signs
root = Tkinter.Tk()
root.withdraw()
file = tkFileDialog.askopenfilename(title='ATT spectrum xlsx')
try:
    #read workbook
    wb = px.load_workbook(file, use_iterators = True)
    # set ws to active workbook, active sheet
    ws = wb.active
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
    
#dictionaries to hold desc, county, state, fips, total spectrum, call sign
desc = dict()
county = dict()
state = dict()
spectrum = dict()
call = dict()

# first line is header so skip it
first = 1
i=0

for row in ws.iter_rows():
    if first == 1:
        first = 0
        continue
    fips = str(row[3].value)
    if fips not in county:
        temp = row[0].value
        desc[fips] = temp.replace('"','')
        temp = row[1].value
        county[fips] = re.sub('[^a-zA-Z0-9 \n\.]', '', temp)    # some county names have special characters
        state[fips] = row[2].value
        spectrum[fips] = row[4].value
        temp = row[5].value
        call[fips] = temp.strip()
    else:
        spectrum[fips] = str(float(row[4].value) + float(spectrum[fips]))
        temp = str(row[5].value)
        if temp not in call[fips]:
            call[fips] = temp.strip() + "," + call[fips]
            
# file header: Radio Service Desc	County	State	FIPS Code	Total Spectrum	Call Sign
whand.write('Radio Service Desc	County	State	FIPS Code	Total BW	Call Sign\n')

for key in desc:
##    print desc[key] + '\n'
##    print county[key] + '\n'
##    print state[key] + '\n'
##    print key + '\n'
##    print spectrum[key] + '\n'
##    print call[key] + '\n'
    whand.write(desc[key] + '\t' + county[key] + '\t' + state[key] + '\t' + key + '\t' + spectrum[key] + '\t' + call[key] + '\n')
    
whand.close()
