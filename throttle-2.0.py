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
file = tkFileDialog.askopenfilename(title='IMSI key NTUA Customers')
try:
    wb = px.load_workbook(file, use_iterators = True)
    # set ws to active workbook, active sheet
    ws = wb.get_sheet_by_name(name = 'IMSI_Key')
except:
    print "bad NTUA Tier Throttle file name"
    exit()

# make directory of first file the new default directory
os.chdir(os.path.dirname(file))

# Open csv spreasheet with usage data
root = Tkinter.Tk()
root.withdraw()
myFormats = [
    ('csv','*.csv'),
    ]
file = tkFileDialog.askopenfilename(filetypes = myFormats, title='NTUA Usage data in csv format')
try:
    usagefhand = open(file)
except:
    print "bad file name"
    exit()

# get saveas filename for output
root = Tkinter.Tk()
root.withdraw()
myFormats = [
    ('csv','*.csv'),
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

# dictionary for IMSI and rate plan
ratePlan = {}
#dictionary for IMSI - daily usage.  Use sets the initial sums to zero
dailySum = {}
#dictionary for start day
startDay = {}

lineNo = 1
for row in ws.iter_rows():    # Read the IMTS key customer spreadsheet
    lineNo += 1
    if lineNo > 2:      # skip header
        IMSI = str(row[35].value)
        IMSI = IMSI.strip()
        if len(IMSI) == 15:
            rawratePlan = str(row[1].value)
            rawratePlan = rawratePlan.strip()
            rawstartDay = str(row[15].value).strip()
            #print "IMSI: " + IMSI + " rawratePlan: " + rawratePlan + " rawstartDay: " + rawstartDay
            ratePlan[IMSI] = rawratePlan
            startDay[IMSI] = int(rawstartDay)
            dailySum[IMSI] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# now go through the usage data and summarize usage into dailySum dictionary
lineNo = 1
for row in usagefhand:       # iterate through rows of usage data
    lineNo += 1
    if lineNo > 2:      # skip header
        fields = row.split(",")
        #print fields[46] + " , " + fields[11] + " , " + fields[38]
        IMSI = fields[46].strip()       # customer IMSI
        usage = long(fields[11].strip())      # DL data usage for the hour
        day = fields[38].strip()     # day of month from usage data
        day = int(day[8:11])
        #print "IMSI: " + IMSI + " usage: " + str(usage) + " day: " + str(day) + " fields[38]: " + fields[38]
        if IMSI in startDay:
            if day < startDay[IMSI]:            # using the first day of the billing cycle as day 1 in list
                normalDay = day - startDay[IMSI] + 30 + 1
            if day >= startDay[IMSI]:
                normalDay = day - startDay[IMSI] + 1
            dailySum[IMSI][normalDay] = dailySum[IMSI][normalDay] + usage
            dailySum[IMSI][0] = dailySum[IMSI][0] + usage
            #print "Fields[38], normalDay: " + fields[38] + ", " + str(normalDay) + " , " + str(startDay[IMSI]) + " , " + str(day)
            #print IMSI + " , " + str(normalDay) + " , " + str(dailySum[IMSI])
        
#print dailySum        
for key, ds in dailySum.iteritems():         # write out the results
    whand.write(key + "," + ratePlan[key])
    for d in ds:
        whand.write("," + str(d))
    whand.write("\n")
    

whand.close()       # close output file
