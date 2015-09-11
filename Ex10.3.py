# tuples in chapter 10
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))  # create list of tuples with length and word
t.sort(reverse=True)   # sort list, uses first value of tuple
print t
res = list()
for length, word in t:  # list of tuples has two values, length and word
    res.append(word)
print res

a='a'
b='b'
a,b=b,a   # swaps values of a and b
print a,b

d = {'a':10, 'b':1, 'c':22}
t = d.items()  # items method returns a list of tuples
print t
t.sort()
print t

#print all items in dictionary and sort by using a list of tuples
l=list()
for key,val in d.items():
    l.append((val,key))
print "unsorted: ", l
l.sort(reverse = True)
print "sorted: ",l
