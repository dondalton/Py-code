#!/usr/bin/python
#multithreaded Collatz conjecture
import Queue
import threading
import time
global max, maxx
max = 0
maxx = 0

def collatz(x):
    global max, maxx
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

inp = raw_input("Start Number: ")
startNo = int(inp)
inp = raw_input("Stop Number: ")
stopNo = int(inp)

##for x in xrange(startNo, stopNo):
##    collatz(x)
##
##print "Max: %s, X: %s" %(max,maxx)

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            collatz(data)
            print "%s processing %s" % (threadName, data)
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4","Thread-5","Thread-6","Thread-7"]
nameList = list(range(startNo, stopNo))
queueLock = threading.Lock()
workQueue = Queue.Queue(100)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
print "Max: %s, X: %s" %(max,maxx)
print "Exiting Main Thread"
