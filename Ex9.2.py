#Excercise 9.2
# count the number of times each From line has a particular day of week
import string

fname = raw_input("File name: ")
try:
    fhand = open(fname)
except:
    print "bad file name"
    exit()

count = dict()
dow = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
for line in fhand:
    line = line.translate(None,string.punctuation)
    words = line.split()
    #print "len of words: ",len(words)
    if len(words) > 2:
        #print "words[0] ",words[0]
        #print words[2] in dow
        if words[0] == 'From' and words[2] in dow:
            count[words[2]] = count.get(words[2],0) + 1
print count

# Excercise 9.5
# now count number of emails from each domain and print the highest number
fhand = open(fname)
countd=dict()
for line in fhand:
    words = line.split()
    if len(words) > 1 and words[0] == 'From:':
        domain = words[1].split('@')
        #print domain[1]
        countd[domain[1]] = countd.get(domain[1],0) + 1

print countd
