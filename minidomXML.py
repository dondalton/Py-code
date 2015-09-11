#import easy to use xml parser called minidom:
from xml.dom.minidom import parseString
#all these imports are standard on most modern python implementations
 
#open the xml file for reading:
file = open('pajarito.xml','r')
#convert to string:
data = file.read()
#close file because we dont need it anymore:
file.close()
#parse the xml you got from the file
dom = parseString(data)
#retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
xmlTag = dom.getElementsByTagName('database')[0].toxml()
#strip off the tag (<tag>data</tag>  --->   data):
xmlData=xmlTag.replace('<row>','').replace('</row>','')
xmlData=xmlData.replace('<v>',' ').replace('</v>',' ')
xmlData=xmlData.replace('<database>','').replace('</database>','')
xmlData=xmlData.replace('<!--',' ').replace('-->',' ')
#print out the xml tag and data in this format: <tag>data</tag>

#print xmlData
xmlsplit = xmlData.split(' ')
print xmlsplit
