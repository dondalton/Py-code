fname = raw_input('Enter file name: ')
fwrite = raw_input('Enter save name: ')
try:
    fhand = open(fname)
    whand = open(fwrite,'w')
except:
    print "bad file name"
    exit()
sitelist = dict()
first = 1
for line in fhand:
    if first == 1:  # first line is for headers
        first = 0
        continue
    words = line.split(',')
    btsno = words[0].rstrip()
    carrier = words[1].rstrip()
    if btsno not in sitelist:
        sitelist[btsno] = carrier
    else:
        if carrier not in sitelist[btsno]:
            sitelist[btsno] = sitelist[btsno] + "_" + carrier

print sitelist
for key in sitelist:
    whand.write( key + "," + sitelist[key] + "\n")

whand.close()
fhand.close()
