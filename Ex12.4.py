#Ex12.4
import urllib
from bs4 import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the paragraph tags
tags = soup('p')
#print tags
for tag in tags:
   print tag.get('style', None)  #print paragraph tags related to style
