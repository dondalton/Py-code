import sys

fname = raw_input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print "bad file name"
    exit()

for line in fhand:
    words = line.split()
    process = words[1]
    print "kill -9 ",process

fhand.close()
