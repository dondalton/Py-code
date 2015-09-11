inp = raw_input("Start Number: ")
startNo = int(inp)
inp = raw_input("Stop Number: ")
stopNo = int(inp)
max = 0
maxx = 0
for x in xrange(startNo, stopNo):
    start = x
    counter = 0
    while x != 1:
        if x/2 == x/2.0:
            x = x/2
        else:
            x = x * 3 + 1
        counter = counter + 1
        if counter > max:
            max = counter
            maxx = start
        #print x, counter
    #print "Start number: %s, Counter = %s" %(start,counter)
print "Max: %s, X: %s" %(max,maxx)
