import time
epoch = time.time()

def minimize1():
    current = yield
    while True:
        for i in range(1,100000000):
            x = i
        value = yield current
        current = min(value, current)

def minimize2():
    current = yield
    while True:
        for i in range(1,100000000):
            x = i
        value = yield current
        current = min(value, current)

def minimize3():
    current = yield
    while True:
        for i in range(1,100000000):
            x = i
        value = yield current
        current = min(value, current)

def minimize4():
    current = yield
    while True:
        for i in range(1,100000000):
            x = i
        value = yield current
        current = min(value, current)

it1 = minimize1()
next(it1)            # Prime the generator
it2 = minimize2()
next(it2)            # Prime the generator
it3 = minimize3()
next(it3)            # Prime the generator
it4 = minimize4()
next(it4)            # Prime the generator

epoch = time.time()
print "localtime: ",time.strftime("%a, %d %b %Y %H:%M:%S +0000",time.localtime(epoch))
x1 = it1.send(1)
print "x1"
x2 = it2.send(40)
print "x2"
x3 = it2.send(20)
print "x3"
x4 = it3.send(-4)
print "x4"

epoch = time.time()
print "localtime: ",time.strftime("%a, %d %b %Y %H:%M:%S +0000",time.localtime(epoch))

print x1
print x2
print x3
print x4

epoch = time.time()
print "localtime: ",time.strftime("%a, %d %b %Y %H:%M:%S +0000",time.localtime(epoch))

print(it1.send(10))
print(it2.send(4))
print(it3.send(22))
print(it3.send(-1))
epoch = time.time()
print "localtime: ",time.strftime("%a, %d %b %Y %H:%M:%S +0000",time.localtime(epoch))
