# define function
def computepay(x,y):
    if (x <= 40):
        pay = x * y
    else:
        pay = (x - 40) * 1.5 * y + 40 * y
    # return value from fucntion
    return pay
    
good = True
while(good):
    try:
        # read from stdin
        input = raw_input("Enter Hours:\n")
        input2 = raw_input("Enter rate:\n")
        hours = int(input)
        rate = int(input2)
        good = False
    except:
        print "No pay for you"
pay = computepay(hours,rate)        
print "Pay = ",pay
   
# random value generator
import random
for i in range(10):
    # random value from 0 to 1
    print random.random()   
for i in range(10):
    #random integer from start to end, not includeing end value
    print random.randint(1,100)
    
name = "Don Dalton"
# random letter from string
print random.choice(name)

name = raw_input("String: \n")
# print string one letter per line
index = 0
while index < len(name):
    letter = name[index]
    print letter
    index = index + 1

print
#print string one letter per line in reverse order
index = -1    
while index >= len(name) * -1:
    letter = name[index]
    print letter
    index = index - 1
    
print name

# extract the email address from string
stuff = 'Don Dalton ddalton@atni.com time and date'
atpos = stuff.find('@')
atposs = stuff.find(' ',atpos)
index = atpos
while index > 0:
	index = index - 1
	if stuff[index] == ' ':
		break
print stuff[index + 1:atposs]

#extract value after ":"
str ='X-DSPAM-Confidence: 0.8475'
atpos = str.find(':')
digits = str[atpos + 1:].strip()
print digits
floater = float(digits)
print type(floater)
print floater

# chapter 7
# enter filename
fname = raw_input('Enter File name: ')
try:
    fhand = open(fname)
    #fhand = open('C:\Users\DDalton\Documents\python\Infomatics\mbox.txt')
except:
        print ('file cannot be opened')
        exit()
#print file handle
print fhand
#count lines in file
count = 0
for line in fhand:
    count = count + 1
print 'Line Count: ', count
#read whole file into variable
fhand = open('C:\Users\DDalton\Documents\python\Infomatics\mbox.txt')
inpu = fhand.read()
print len(inpu)
print inpu[:20]
#print if line starts with "From:"
fhand = open('C:\Users\DDalton\Documents\python\Infomatics\mbox.txt')
for line in fhand:
        #strip whitespace and newline from right side of string
        line = line.rstrip()
        #if line.startswith('From:'):
                #print line
        if line.find('@uct.ac.za') > 0:
                print line
#close file
fhand.close()
#write to file
line1 = 'testing 1 2 3'
#open with 'w' to write to file
fout = open('junk.txt','w')
print fout
fout.write(line1)
fout.close()

# change and check current dir
import os
print os.getcwd()
os.chdir('Infomatics')  # change current dir
print os.getcwd()
os.chdir('..')
print os.getcwd()

#print tabs, newlines and hidden chars
s = '1 2\t 3\n 4'
print s
print repr(s)

#traverse a list without index
cheeses = ['Cheddar', 'Edam', 'Gouda']
for cheese in cheeses:
        print cheese
#with index
for i in range(len(cheeses)):
        print cheeses[i]
        
#list can contain lists, but length of list does not count sublists
cheeses = ['Cheddar', 'Edam', 'Gouda', ['Cheddar', 'Edam', 'Gouda']]
print "Cheese list: ",cheeses
print "length of cheeses: ",len(cheeses)
#add concats lists and multiply creates n copies
print "add cheeses: ",cheeses + cheeses
print "triple cheeses: ",cheeses * 3
#append to list
cheeses.append('cheddar')
print "append cheeses: ",cheeses
cheesy = ['squeeze','american']
cheeses.extend(cheesy)
print "extend cheeses: ",cheeses
cheeses.sort()
print "sorted cheeses: ",cheeses
# pop removes element and places in variable
x = cheeses.pop(1)
print "popped value: ", x
print "cheeses post pooping: " , cheeses
#del removes element, can delete multiple with del cheeses[1:5]
del cheeses[1]
print "deleted cheeses: ",cheeses
#remove specific value by value not index
cheeses.remove('cheddar')
print "cheese without cheddar: ", cheeses
#can do len, max, min, sum for lists (sum only works for numbers)

s = 'of all the fishes'
t = list(s)
print "string converted to list: ",t
t = s.split()   # can put a delimtiter in the empty brackets
print "string converted to list using split: ",t
# split on word boundaries
word = s.split()
print word[3] # prints "fishes"

# a is b will be true if a and b point to the same object
# chop function deletes first and last element of a list
def chop(t):
    del t[len(t) - 1]
    del t[0]

s = [1,2,3,4,5]
chop(s)
print s   # prints [2,3,4]

# list functions do not return a value other than None.  t = t.sort() assigns "none" to t


