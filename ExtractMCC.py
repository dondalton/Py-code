import re
fname = raw_input('Enter file name: ')
fwriteSBA = raw_input('Enter SBA save name: ')
fwriteComm = raw_input('Enter Commnet save name: ')
try:
    fhand = open(fname)
    whandSBA = open(fwriteSBA,'w')
    whandComm = open(fwriteComm,'w')
except:
    print "bad file name"
    exit()

for line in fhand:
    words = re.split('\t+',line)
    lat = words[1].strip()
    lon = words[2].strip()
    if len(words) > 4:
        mcc = words[4].strip()
    if len(words) > 7 and int(float(words[7].strip())) == float(words[7].strip()) and float(words[7].strip()) > 0 and float(words[7].strip()) < 513:
        SC = words[7].strip()
        
##    for word in words:
##        print word + ","
##    print "\n"
##    print "lat: " + lat + " lon: " + lon + " mcc: " + mcc + " SC: " + SC
        
    if mcc == "40" and float(lat) > 1.0 and float(lon) < -1.0:
        #print "Comm lat: " + lat + " lon: " + lon + " mcc: " + mcc + " SC: " + SC
        whandComm.write(lat + "," + lon + "," + mcc + "," + SC + "\n")
    if mcc == "320" and float(lat) > 1.0 and float(lon) < -1.0:
        #print "SBA lat: " + lat + " lon: " + lon + " mcc: " + mcc
        whandSBA.write(lat + "," + lon + "," + mcc + "," + SC + "\n")
        
whandComm.close()
whandSBA.close()
