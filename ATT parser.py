import os

os.chdir("C:\Users\DDalton\Documents\RF design\ATT Northern AZ overlay\spectrum map")
print "Current directory: " + os.getcwd()

fname = raw_input('Enter Spectrum tab delimeted file name: ')
try:
    fhand = open(fname)
except:
    print "bad file name"
    exit()

fwrite = raw_input('Enter text output file name: ')
try:
    whand = open(fwrite,'w')
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

for line in fhand:
    if first == 1:
        first = 0
        continue
    words = line.split("\t")
    fips = words[3]
    if fips not in county:
        desc[fips] = words[0].replace('"','')
        county[fips] = words[1]
        state[fips] = words[2]
        spectrum[fips] = words[4]
        call[fips] = words[5].strip()
    else:
        spectrum[fips] = str(float(words[4]) + float(spectrum[fips]))
        if words[5].strip() not in call[fips]:
            call[fips] = words[5].strip() + "," + call[fips]
            
# file header: Radio Service Desc	County	State	FIPS Code	Total Spectrum	Call Sign
whand.write('Radio Service Desc	County	State	FIPS Code	Total BW	Call Sign\n')

for key in desc:
    whand.write(desc[key] + '\t' + county[key] + '\t' + state[key] + '\t' + key + '\t' + spectrum[key] + '\t' + call[key] + '\n')
    
fhand.close()
whand.close()
