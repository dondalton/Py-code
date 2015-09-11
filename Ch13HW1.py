import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)


    results = tree.findall('result')  # breaks down to highest level, results
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print 'lat',lat,'lng',lng
    print location

    # finds short code for country
    print
    print
    results = tree.findall('result/address_component') # breaks down to next level of tree
    for item in results:
        #print item.find('type').text
        if (item.find('type').text == 'country'):
            print item.find('short_name').text
            
##<?xml version="1.0" encoding="UTF-8"?>
##<GeocodeResponse>
## <status>OK</status>
## <result>        
##<address_component>
##   <long_name>Slovenia</long_name>
##   <short_name>SI</short_name>
##   <type>country</type>
##   <type>political</type>
##</address_component>
