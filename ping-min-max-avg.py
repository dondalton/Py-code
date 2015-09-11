from datetime import datetime
import sys
import os
from os.path import join

for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt') :
            fname = filename
            print fname[:-4]

            try:
                fhand = open(fname)
            except:
                print "bad file name"
                exit()

            first = 1
            count = 0
            max = 0
            min = 999999
            sum = 0
            for line in fhand:
                if first == 1:
                    first = 0
                    continue
                words = line.split()
                temp = words[7].split("=")
                rtt = float(temp[1])
                sum += rtt
                count += 1
                if rtt < min:
                    min = rtt
                if rtt > max:
                    max = rtt
            average = sum / count
            print "rtt min/avg/max = ",min,"/",average,"/",max,"\n"

fhand.close()
