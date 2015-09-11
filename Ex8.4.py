#excercise 8.4
sorted = []
fname = raw_input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print "bad file name"
    exit()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in sorted:
            sorted.append(word)
sorted.sort()
print sorted

#excercise 8.6
inpoo = ""
numlist = []
while not inpoo == "done":
    inpoo = raw_input("Enter a number: ")
    if inpoo == "done":
        break
    numlist.append(inpoo)
print "Min: ", min(numlist)
print "Max: ",max(numlist)
