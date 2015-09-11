import os       # library for changing directory calls
import Tkinter, tkFileDialog   # library for open and save file dialogs
from Tkinter import *
import openpyxl as px     # read xlsx library
import re

# make the home directory the starting point of the open file dialog
from os.path import expanduser
home = expanduser("~")     # get default directory of user
os.chdir(home)
os.chdir("./Documents")
os.chdir('C:\Users\DDalton\Documents\planning\LTE customer data')

# Open spreadsheet
root = Tkinter.Tk()
root.withdraw()
file = tkFileDialog.askopenfilename(title='Open Spreadsheet')
try:
    #read workbook
    wb = px.load_workbook(file, use_iterators = True)
    # set ws to active workbook, active sheet
    ws = wb.get_sheet_by_name(name = 'NTUA_Dashboard_TotalActiveSubsL')
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

whand.write( "Latitude, Longitude\n")
lineno = 0
for row in ws.iter_rows():   # read line by line through spreadsheet
    lineno += 1
    if lineno > 1:
        try:
            location = row[43].value
            try:
                location = re.sub('\xf8'," ",location)
            except:
                location = str(location)
        
            if not(re.search('[\\\,\/,s]\s*',location)):      # most lines are delimited with "\", "/" or space, if no delimeter, add one
                location = re.sub(' -1','/-1',location)       # adds a / before a -1 assuming that is the start of the longitude

            location = location.strip()     #delete leading and trailing whitespace
            location = location.strip("/")      # delete leading and trailing /
            location = location.strip("\\")     # delete leading and trailing backslash
            location = location.strip(".")      # delete leading and trailing decimal points
            location = re.sub("--","",location)     # delete and double dashes
            location = re.sub("//","/",location)    # make and double slashes into a single delimeter
            location = re.sub("N1","N/-1",location)

            if re.search('[\\\,\/,s]\s*',location):     # split on \, /, or space
                latString = re.split(r'[\\,\/,s]\s*',location)[0]
                lonString = re.split(r'[\\,\/,s]\s*',location)[1]
                latString = re.sub('[^0123456789\.]'," ",latString)     # get ride of non-numeric values
                lonString = re.sub('[^-0123456789\.]'," ",lonString)
                
                latString = re.sub(r'^((.*?\..*?){1})\.', r'\1', latString)     # get ride of extra decimal points
                lonString = re.sub(r'^((.*?\..*?){1})\.', r'\1', lonString)
                #lonString = re.sub(r'^((.*?-.*?){1})\.', r'\1', lonString)   # get ride of trailing minus sign

                if latString[2] == " " and latString[5] == " ":   #convert DMS format latitude to decimal
                    latString = str(float(latString[0:2]) + float(latString[3:5])/60.0 + float(re.sub('[^0123456789\.]',"",latString[6:]))/3600.0)
                if lonString[3] == " " and lonString[6] == " ":    # convert DMS format longitude to decimal, does not have a negative sign
                    lonString = str(-1 * (float(lonString[0:3]) + float(lonString[4:6])/60.0 + float(re.sub('[^0123456789\.]',"",lonString[7:]))/3600.0))
                if lonString[4] == " " and lonString[7] == " ":      # convert DMS format longitude to decimal, does have a negative sign
                    lonString = str(float(lonString[0:4]) + float(lonString[5:7])/60.0 + float(re.sub('[^0123456789\.]',"",lonString[8:]))/3600.0)

                if float(lonString) > 0:
                    lonString = str(float(lonString) * -1)
                
                latString = latString.replace(" ","")   # clean up whitespaces
                lonString = lonString.replace(" ","")
                
                decPos = latString.find(".")   # sometimes decimal point is in the wrong place
                if decPos != 2:
                    if decPos > 2:
                        latString = str(float(latString) / (10 ** (decPos - 2)))
                    if decPos == -1:
                        latString = str(float(latString) / (10 ** (len(latString) - 2)))
                        
                decPos = lonString.find(".")   # sometimes decimal point is in the wrong place
                if decPos != 4:
                    if decPos > 4:
                        lonString = str(float(lonString) / (10 ** (decPos - 4)))
                    if decPos == -1:
                        lonString = str(float(lonString) / (10 ** (len(lonString) - 4)))
                whand.write(latString + "," + lonString + "\n")
            else:
                whand.write("0,0" + "\n")     # no delimeter
        except:
            whand.write("0,0" + "\n")

whand.close()
