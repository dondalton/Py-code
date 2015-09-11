#Ex 10.2
print "Excercise 10.2"
fname = "./infomatics/mbox-short.txt"
try:
    fhand = open(fname)
except:
    print "bad file name"
    exit()

d = dict()
for line in fhand:  #read lines in file
    words = line.split()   # split onto words on space
    if len(words) > 5:      # can do words[0] if line length is zero
        if words[0] == "From":
            hours = words[5].split(":")    # time is hh:mm:ss
            hour = hours[0]
            if hour in d:     # put hour and count in dictionary
                d[hour] += 1
            else:
                d[hour] = 1

l = list()
for key,value in d.items():      # take values from dictionary and put in list of tuples
    l.append((key,value))
l.sort()      # sort list of tuples by first value (hour)
for l2 in l:     # go through list and print key and value
    print l2[0], l2[1]

#Excercise 10.3
print "Excercise 10.3, letter frequency in file"
import string
fname = "./infomatics/romeo.txt"
try:
    fhand = open(fname)
except:
    print "bad file name"
    exit()

d = dict()
for line in fhand:  #read lines in file
    line = line.translate(None,string.punctuation)
    line = line.strip()
    line = line.lower()
    index = 0
    while index < len(line):
        letter = line[index]
        if letter in d and not letter == ' ':
            d[letter] += 1
        elif not letter == ' ':
            d[letter] = 1
        index += 1
        
l = list()
for key,value in d.items():      # take values from dictionary and put in list of tuples
    l.append((key,value))
l.sort()      # sort list of tuples by first value (hour)
for l2 in l:     # go through list and print key and value
    print l2[0], l2[1]
