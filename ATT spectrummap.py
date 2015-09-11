import os       # library for changing directory calls
import Tkinter, tkFileDialog   # library for open and save file dialogs

# make the home directory the starting point of the open file dialog
from os.path import expanduser
home = expanduser("~")     # get default directory of user
os.chdir(home)

# open tab delimeted file with spectrum holdings:
# Radio Service Desc	County	State	FIPS Code	Total BW	Call Signs
root = Tkinter.Tk()
root.withdraw()
file = tkFileDialog.askopenfilename(title='tab delimited spectrum holdings')
try:
    fhand = open(file)
except:
    print "bad file name"
    exit()

# make directory of first file the new default directory
os.chdir(os.path.dirname(file))

# get county map kml file with FIPS codes
root = Tkinter.Tk()
root.withdraw()
file = tkFileDialog.askopenfilename(title='Enter County map kml file name')
try:
    shand = open(file)
except:
    print "bad file name"
    exit()

# get saveas filename for kml output
root = Tkinter.Tk()
root.withdraw()
myFormats = [('kml','*.kml'),]

fileName = tkFileDialog.asksaveasfilename(filetypes=myFormats ,title="Save the kml as...")
try:
    whand = open(fileName,'w')
except:
    print "bad file name"
    exit()

#define a dictionary to hold FIPS code to coordiantes
countydict = dict()

# read in county map to get FIPS and coordinates in a dictionary called countydict
for line in shand:
    if 'State County FIPS' in line:
        line = next(shand)
        temp = line.split("[")[2]
        fips = temp.split("]")[0]
        # loop until we find coordinates, then read coordinates into dictionary with FIPS as key
        while "<outerBoundaryIs><LinearRing><coordinates>" not in line:
            line = next(shand)
        line = next(shand)    
        coords = line.strip()
        if fips not in countydict:
            countydict[fips] = coords

# read radio service description so that name can be in Document name
first = 1     # first line are headers

for line in fhand:
    if first == 1:
        first = 0
        continue
    words = line.split("\t")
    desc = words[0].replace('"','')
#return to first line in file
fhand.seek(0,0)
    
# write header and style for kml file
whand.write( '<?xml version="1.0" encoding="UTF-8"?>' + '\n')
whand.write( '<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">' + '\n')
whand.write( "<Document>" + '\n')
whand.write( "    <name>" + desc + "</name>" + '\n')

whand.write( '      <StyleMap id="default">' + '\n')
whand.write( '      <Pair>' + '\n')
whand.write( '      	<key>normal</key>' + '\n')
whand.write( '        <styleUrl>#default_normal</styleUrl>' + '\n')
whand.write( '      </Pair>' + '\n')
whand.write( '      <Pair>' + '\n')
whand.write( '        <key>highlight</key>' + '\n')
whand.write( '        <styleUrl>#default_highlight</styleUrl>' + '\n')
whand.write( '      </Pair>' + '\n')
whand.write( '      </StyleMap>' + '\n')

whand.write( '<Style id="default_normal">' + '\n')
whand.write( '    <IconStyle>' + '\n')
whand.write('        <scale>1</scale>' + '\n')
whand.write('        <Icon>' + '\n')
whand.write('            <href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png</href>' + '\n')
whand.write('        </Icon>' + '\n')
whand.write('    </IconStyle>' + '\n')
whand.write('    <LabelStyle>' + '\n')
whand.write('        <scale>0</scale>' + '\n')
whand.write('    </LabelStyle>' + '\n')
whand.write('    <LineStyle>' + '\n')
whand.write('        <color>eeff6600</color>' + '\n')
whand.write('        <width>1</width>' + '\n')
whand.write('    </LineStyle>' + '\n')
whand.write('    <PolyStyle>' + '\n')
whand.write('        <color>99ff6600</color>' + '\n')
whand.write('        <outline>1</outline>' + '\n')
whand.write('        <fill>1</fill>' + '\n')
whand.write('    </PolyStyle>' + '\n')
whand.write('    <BalloonStyle>' + '\n')
whand.write('        <bgColor>00000000</bgColor>' + '\n')
whand.write('        <text>' + '\n')
whand.write('        <![CDATA[' + '\n')
whand.write('        <body bgcolor="#000000" width="100%">' + '\n')
whand.write('        <p><b><font color="#ffffff">$[a/displayName]:</font></b> <font color="#DDDDDD">$[a]</font></p>' + '\n')
whand.write('        <p><b><font color="#ffffff">$[b/displayName]:</font></b> <font color="#DDDDDD">$[b]</font></p>' + '\n')
whand.write('        <p><b><font color="#ffffff">$[c/displayName]:</font></b> <font color="#DDDDDD">$[c]</font></p>' + '\n')
whand.write('        <p><b><font color="#ffffff">$[d/displayName]:</font></b> <font color="#DDDDDD">$[d]</font></p>' + '\n')
whand.write('        <p><b><font color="#ffffff">$[e/displayName]:</font></b> <font color="#DDDDDD">$[e]</font></p>' + '\n')
whand.write('        <p><b><font color="#ffffff">$[f/displayName]:</font></b> <font color="#DDDDDD">$[f]</font></p>' + '\n')
whand.write('        ]]>' + '\n')
whand.write('        </text>' + '\n')
whand.write('    </BalloonStyle>' + '\n')
whand.write('</Style>' + '\n')

whand.write( '<Style id="default_highlight">' + '\n')
whand.write( '    <IconStyle>' + '\n')
whand.write('        <scale>1</scale>' + '\n')
whand.write('        <Icon>' + '\n')
whand.write('            <href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png</href>' + '\n')
whand.write('        </Icon>' + '\n')
whand.write('    </IconStyle>' + '\n')
whand.write('    <LabelStyle>' + '\n')
whand.write('        <scale>0</scale>' + '\n')
whand.write('    </LabelStyle>' + '\n')
whand.write('    <LineStyle>' + '\n')
whand.write('        <color>ddffffff</color>' + '\n')
whand.write('        <width>1</width>' + '\n')
whand.write('    </LineStyle>' + '\n')
whand.write('    <PolyStyle>' + '\n')
whand.write('        <color>ccff6600</color>' + '\n')
whand.write('        <outline>1</outline>' + '\n')
whand.write('        <fill>1</fill>' + '\n')
whand.write('    </PolyStyle>' + '\n')
whand.write('    <BalloonStyle>' + '\n')
whand.write('        <bgColor>00000000</bgColor>' + '\n')
whand.write('        <text>' + '\n')
whand.write('        <![CDATA[' + '\n')
whand.write('        <body bgcolor="#000000" width="100%">' + '\n')
whand.write('        <p><b><font color="#ffffff">$[a/displayName]:</font></b> <font color="#DDDDDD">$[a]</font></p>' + '\n')
whand.write('        <p><b><font color="#ffffff">$[b/displayName]:</font></b> <font color="#DDDDDD">$[b]</font></p>' + '\n')
whand.write('        <p><b><font color="#ffffff">$[c/displayName]:</font></b> <font color="#DDDDDD">$[c]</font></p>' + '\n')
whand.write('        <p><b><font color="#ffffff">$[d/displayName]:</font></b> <font color="#DDDDDD">$[d]</font></p>' + '\n')
whand.write('        <p><b><font color="#ffffff">$[e/displayName]:</font></b> <font color="#DDDDDD">$[e]</font></p>' + '\n')
whand.write('        <p><b><font color="#ffffff">$[f/displayName]:</font></b> <font color="#DDDDDD">$[f]</font></p>' + '\n')
whand.write('        ]]>' + '\n')
whand.write('        </text>' + '\n')
whand.write('    </BalloonStyle>' + '\n')
whand.write('</Style>' + '\n')

# go through all the lines in spectrum allocation and print placemark
# should be tab delimeted file with following fields: Radio Service Desc,County,State,FIPS Code,Total BW,Call Signs
# coordinates printed by looking up fips code in countydict dictionary

first = 1

for line in fhand:
    if first == 1:
        first = 0
        continue
    words = line.split("\t")
    desc = words[0].replace('"','')
    county = words[1]
    state = words[2]
    fips = words[3]
    bw = words[4]
    call = words[5].strip()
    if fips not in countydict:
        print "error: " + county + "  " + fips + '\n'
    else:
        whand.write('    <Placemark>' + '\n')
        whand.write('        <styleUrl>#default</styleUrl>' + '\n')
        whand.write('        <name><![CDATA[' + county + ']]></name>' + '\n')
        whand.write('    \n')
        whand.write('        <ExtendedData>' + '\n')
        whand.write('            <Data name=\'a\'>' + '\n')
        whand.write('                <displayName><![CDATA[Spectrum]]></displayName>' + '\n')
        whand.write('                <value><![CDATA[' + desc + ']]></value>' + '\n')
        whand.write('            </Data>' + '\n')
        whand.write('            <Data name=\'b\'>' + '\n')
        whand.write('                <displayName><![CDATA[State]]></displayName>' + '\n')
        whand.write('                <value><![CDATA[' + state + ']]></value>' + '\n')
        whand.write('            </Data>' + '\n')
        whand.write('            <Data name=\'c\'>' + '\n')
        whand.write('                <displayName><![CDATA[County]]></displayName>' + '\n')
        whand.write('                <value><![CDATA[' + county + ']]></value>' + '\n')
        whand.write('            </Data>' + '\n')
        whand.write('            <Data name=\'d\'>' + '\n')
        whand.write('                <displayName><![CDATA[FIPS]]></displayName>' + '\n')
        whand.write('                <value><![CDATA[' + fips + ']]></value>' + '\n')
        whand.write('            </Data>' + '\n')
        whand.write('            <Data name=\'e\'>' + '\n')
        whand.write('                <displayName><![CDATA[Bandwidth]]></displayName>' + '\n')
        whand.write('                <value><![CDATA[' + bw + ']]></value>' + '\n')
        whand.write('            </Data>' + '\n')
        whand.write('            <Data name=\'f\'>' + '\n')
        whand.write('                <displayName><![CDATA[Call Sign]]></displayName>' + '\n')
        whand.write('                <value><![CDATA[' + call + ']]></value>' + '\n')
        whand.write('            </Data>' + '\n')
        whand.write('        </ExtendedData>' + '\n')
        whand.write('        <MultiGeometry>' + '\n')
        whand.write('            <Polygon>' + '\n')
        whand.write('              <outerBoundaryIs><LinearRing><coordinates>' + '\n')
        whand.write('                  ' + countydict[fips] + '\n')
        whand.write('              </coordinates></LinearRing></outerBoundaryIs>' + '\n')
        whand.write('            </Polygon>' + '\n')
        whand.write('        </MultiGeometry>' + '\n')
        whand.write('    </Placemark>' + '\n')
    
# write lines to close kml
whand.write('  </Document>')
whand.write('</kml>')

# close files
whand.close()
fhand.close()
