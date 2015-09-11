import xml.etree.ElementTree as ET
data = '''
<person>
<name>Chuck</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes"/>
</person>'''
tree = ET.fromstring(data)
print 'Name:',tree.find('name').text
print 'Attr:',tree.find('email').get('hide')
print tree.find('phone').get('type')


input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
    <abusers>
      <abuser>Joan</abuser>
    </abusers>
  </users>
  <people>
    <name>Don</name>
  </people>
</stuff>'''
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print 'User count:', len(lst)
for item in lst:
    print 'Name', item.find('name').text
    print 'Id', item.find('id').text
    print 'Attribute', item.get('x')

print
print

lst = stuff.findall('people')
print 'People count',len(lst)
for item in lst:
    print 'Name: ',item.find('name').text

print
print

lst = stuff.findall('users/abusers')
print 'Abuser count',len(lst)
for item in lst:
    print 'Abuser: ',item.find('abuser').text

print
print "JSON"

#JSON
import json
input = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''
info = json.loads(input)
print 'User count:', len(info)
print info[0]                 # prints first item in list which is a dictionary
for item in info:    # each item is a dictionary
    print 'Name', item['name']   # returns value for dictionary attribute 'name'
    print 'Id', item['id']
    print 'Attribute', item['x']
