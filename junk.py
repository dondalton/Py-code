nbrlist= []
x = "10-1"
y = "11-1"
z = "12-1"
nbr = [x,y]
nbr2 = [x,z]
nbr3 = [x,y]
nbrlist.append(nbr)
nbrlist.append(nbr2)
print nbrlist
if nbr3 in nbrlist:
    print "yes"
