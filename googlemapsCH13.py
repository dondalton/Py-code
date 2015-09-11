# google maps JSON interface
# request: http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Ann+Arbor%2C+MI
import urllib
import json
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    url = serviceurl + urllib.urlencode({'sensor':'false','address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue
    print json.dumps(js, indent=4)
    lat = js["results"][0]["geometry"]["location"]["lat"]  # the [0] is the first element in list
    lng = js["results"][0]["geometry"]["location"]["lng"]  # probably only returns on list element
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location
    print
    print
