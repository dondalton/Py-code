from datetime import datetime

fname = raw_input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print "bad file name"
    exit()

fwrite = raw_input('Enter save name: ')
whand = open(fwrite,'w')

for line in fhand:
   words = line.split()
   temp = words[6].split("=")
   rtt = temp[1]
   outpoo = rtt + "\n"
   whand.write(outpoo)

whand.close()
fhand.close()
