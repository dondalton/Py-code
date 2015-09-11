import sys

Srealms = dict()
Vrealms = dict()
Crealms = dict()
remainder = dict()
count = 0
line = sys.stdin.readline()   # get headers
while 1:
    count += 1
    line = sys.stdin.readline()
    if not line: break
    if len(line) < 1: continue
    cols = list(line.split(','))
    if len(cols) > 50 and cols[5].find('204.133') > 0 and len(cols[1]) > 11 and len(cols[49]) > 4:
        BSID = cols[1]
        realm = cols[49].lower()
        if realm.find('sprint') > 0:
            if BSID not in Srealms:
                Srealms[BSID] = 1
            else:
                Srealms[BSID] += 1
        elif realm.find('vz') > 0:
            if BSID not in Vrealms:
                Vrealms[BSID] = 1
            else:
                Vrealms[BSID] += 1
        elif realm.find('choice') > 0:
            if BSID not in Crealms:
                Crealms[BSID] = 1
            else:
                Crealms[BSID] += 1
        else:
            if realm not in remainder:
                remainder[realm] = 1
            else:
                remainder[realm] += 1

print count," rows processed"
print

Sout = open('SprintBSID.txt','w')
for key in Srealms:
    outpoo = key
    outpoo += ","
    outpoo += str(Srealms[key])
    outpoo += "\n"
    Sout.write( outpoo )
Sout.close()

Vout = open('VerizonBSID.txt','w')
for key in Vrealms:
    outpoo = key
    outpoo += ","
    outpoo += str(Vrealms[key])
    outpoo += "\n"
    Vout.write( outpoo )
Vout.close()

Cout = open('ChoiceBSID.txt','w')
for key in Crealms:
    outpoo = key
    outpoo += ","
    outpoo += str(Crealms[key])
    outpoo += "\n"
    Cout.write( outpoo )
Cout.close()

print "missing realm\tcount"
for key in remainder:
    print key, "\t", remainder[key]

