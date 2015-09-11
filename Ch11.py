# -*- coding: cp1252 -*-
import re
fhand = open('./infomatics/mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('^From',line):  # could use python .startswith()
        print line

fhand = open('./infomatics/mbox-short.txt')
for line in fhand:
    line = line.rstrip()            # search returns a string
    if re.search('From:.+@',line):  # match one or more characters between From: and @
        print line                  # * matches zero or more characters
                                    # * and + apply to the character to the left
        
# \S means any non whitespace character so this matches anything with something 
# in [a-zA-Z0-9] and then zero or more non whitespace.
#
    lst = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)  # findall returns a list
    if len(lst) > 0:
        print lst

fhand = open('./infomatics/mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    # start with 'X', then zero or more non-whitespace, then ': '
    #then one or more numbers or periods
    if re.search('^X\S*: [0-9.]+',line):
        print line

hand = open('./infomatics/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # in a normal RE, the parens are ignored.  In findall, it only returns what is in parens
    x = re.findall('^X\S*: ([0-9.]+)',line)
    if len(x) > 0:
        print "only num: ",x
        
hand = open('./infomatics/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # get the hour from the 'From:' line
    x = re.findall('^From .* ([0-9][0-9]):',line)
    if len(x) > 0:
        print "hour: ",x


## Excercise 11.1
# match 'New Revision: 12345' and exract the number.  Then print average of numbers
print
print
sum = 0
count = 0
hand = open('./infomatics/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9]+)',line)
    if len(x) > 0:
        print x
        sum = sum + int(x[0])
        count += 1
print "Sum: ",sum,"  Average: ",float(sum)/float(count)
    
