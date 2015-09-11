import xml.etree.ElementTree as ET

class PIParser(ET.XMLTreeBuilder):

   def __init__(self):
       ET.XMLTreeBuilder.__init__(self)
       # assumes ElementTree 1.2.X
       self._parser.CommentHandler = self.handle_comment
       self._parser.ProcessingInstructionHandler = self.handle_pi
       self._target.start("document", {})

   def close(self):
       self._target.end("document")
       return ET.XMLTreeBuilder.close(self)

   def handle_comment(self, data):
       self._target.start(ET.Comment, {})
       self._target.data(data)
       self._target.end(ET.Comment)

   def handle_pi(self, target, data):
       self._target.start(ET.PI, {})
       self._target.data(target + " " + data)
       self._target.end(ET.PI)

def parse(source):
    return ET.parse(source, PIParser())

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
    
##for ping in root.findall('./rra/cdp_prep/ds'):
##    prim = ping.find('primary_value').text
##    print prim

for ping in root.findall('row'):
    v = ping.find('v').text
    print v
    print c

print
print
