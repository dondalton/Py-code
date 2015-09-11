fname = raw_input('Enter file name: ')

fhand = open(fname,"r")
lines =  fhand.read().splitlines()
for i in range(len(lines)):
     if i + 7 < len(lines):
         line = lines[i]
         imsi_line = lines[i+7]
         if "General Page" in line and "719-626-9102" in imsi_line:
             print line
             print imsi_line


