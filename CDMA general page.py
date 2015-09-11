fname = raw_input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print "bad file name"
    exit()

for line in fhand:
    if "IMSI_S: " in line:
        line.strip()
        number = line.split(":")[2].strip()
        print(number)
