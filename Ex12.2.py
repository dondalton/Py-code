# chapter 12, web pages and sockets
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data
mysock.close()

#example 12.3 - get a jpg image from main page and save to file
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')
count = 0
picture = ""
while True:
    data = mysock.recv(5120)
    if ( len(data) < 1): break
    # time.sleep(0.25)     # can pause so the buffer fills to 5120 bytes each recv
    count = count + len(data)  # cumulative count of bytes from recv call
    print len(data), count   # print the number of bytes from the last recv and cumulative
    picture = picture + data

mysock.close()

# find end of header - 2 carriage return/line feeds
pos=picture.find("\r\n\r\n")

print 'Header length',pos
print picture[:pos]     # print from start of get data to end of header
#get rid of header and save picture file
picture = picture[pos+4:]
fhand = open("stuff.jpg","wb")   # saves to C:\python27 by default
fhand.write(picture)
fhand.close()

print
print
print

# Ex 12.8 a better way to read and write the file
# reads entire image into memory, then writes to file
import urllib
img = urllib.urlopen('http://www.py4inf.com/cover.jpg').read()
fhand = open('cover.jpg', 'w')
fhand.write(img)
fhand.close()

# If file is too big for memory, read to buffer, then write to file
import urllib
img = urllib.urlopen('http://www.py4inf.com/cover.jpg')
fhand = open('cover2.jpg', 'w')
size = 0
while True:
    info = img.read(100000)  # read 100k characters into buffer
    if len(info) < 1 : break
    size = size + len(info)
    fhand.write(info)
print size,'characters copied.'
fhand.close()

#Ex. 12.4 urllib - treats web page as file handle.  Does not return header info
import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
    print line.strip()
fhand.close()

print
print
print

#Ex. 12.6 parse for links on a page
import urllib
import re
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()  # read in page
links = re.findall('href="(http://.*?)"', html) # match regex to html variable
for link in links:
    print link

print
print
print

#Ex. 12.7 parsing errored HTML using beautiful soup (installed with pip install beautifulsoup4
# book says "from BeautifulSoup import *", but package is bs4
# BeautifulSoup from crummy.com

import urllib
from bs4 import *
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')
for tag in tags:
    print tag.get('href', None)
