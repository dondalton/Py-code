#Ex 9.1 counts number of occurnaces of each word in file
worddict = dict()
fname = raw_input("File name: ")
try:
    fhand = open(fname)
except:
    print "bad file name"
    exit()
for line in fhand:
    words = line.split()
    for word in words:
        worddict[word] = worddict.get(word,0) + 1

#returns True or False if word is in dictionary
print 'Writing' in worddict

#print entire dictionary
print worddict
print

#print key and value
for key in worddict:
    print key.upper(), worddict[key]
print

#sort and print with counter
from collections import Counter
c = Counter()
# this will sum the values if you have If and if.
for k,v in worddict.items():
    c.update({k.upper(): v})
lst = c.keys()
lst.sort()
for key in lst:
    print key, c[key]
print

#clean up punctuation
import string
fhand = open(fname)
counts = dict()
for line in fhand:
    # translate deletes all characters that match the list string.punctuation
    line = line.translate(None,string.punctuation)
    line = line.lower()    # convert to lower case
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] +=1
print counts
    
