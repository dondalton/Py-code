import time
epoch = time.time()
print "localtime: ",time.strftime("%a, %d %b %Y %H:%M:%S +0000",time.localtime(epoch))
print "GMT time: ",time.strftime("%a, %d %b %Y %H:%M:%S +0000",time.gmtime(epoch))
