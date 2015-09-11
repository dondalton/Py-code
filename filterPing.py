from datetime import datetime
import sys

#fname = raw_input('Enter file name: ')

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
fname = sys.argv[1]
fwrite = sys.argv[2]
print "fname: ", fname
print "fwrite: ",fwrite

try:
    fhand = open(fname)
except:
    print "bad file name"
    exit()

#fwrite = raw_input('Enter save name: ')
whand = open(fwrite,'w')

first = 1

for line in fhand:
    if first == 1:
        first = 0
        continue
    words = line.split()
    time = words[0].replace("[","").replace("]","")
    temp = words[7].split("=")
    rtt = temp[1]
    ttime = datetime.fromtimestamp(float(time))
    tday=ttime.strftime("%Y-%m-%d")
    thour = ttime.strftime("%H:%M:%S")
    justmin = ttime.strftime("%H%M%S")
    outpoo = rtt + " , " + thour + " , " + tday + " , " + time + " , " + justmin + "\n"
    whand.write(outpoo)

whand.close()
fhand.close()
