import os

for (dirname, dirs, files) in os.walk('C:\Users\DDalton\Documents\RF performance\LTE\Oct.20 params'):
    for filename in files:
        filenameFull = os.path.join(dirname,filename)
        print filenameFull
        try:
            fhand = open(filenameFull)
        except:
            print "bad file name: " + filename
        for line in fhand:
            #if 'SubNetwork=100001,MEID=24,ENBFunctionFDD=234' in line:
                #print line
            if 'Chinle' in line:
                print line
