import xml.etree.ElementTree as ET
fname = raw_input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print "bad file name"
    exit()

tree = ET.parse(fhand)
root = tree.getroot()
print root.tag
print root.attrib
for child in root:
    print child.tag, child.attrib
    
for ping in root.findall('./rra/cdp_prep/ds'):
    prim = ping.find('primary_value').text
    print prim

for ping in root.findall('./rra/database/row'):
    v = ping.find('v').text
    print v

print
print

