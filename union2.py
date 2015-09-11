import urllib
import re
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1259449")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1259449' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1240655")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1240655' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1063028")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1063028' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1293458")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1293458' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1256798")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1256798' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1274513")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1274513' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1240656")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1240656' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1229347")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1229347' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1235067")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1235067' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1229343")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1229343' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1063027")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1063027' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1268961")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1268961' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1279505")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1279505' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1285640")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1285640' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1248614")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1248614' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1269575")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1269575' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1272544")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1272544' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1062952")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1062952' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1256626")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1256626' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1008617")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1008617' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1280940")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1280940' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1010152")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1010152' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1256610")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1256610' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1266899")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1266899' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1293448")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1293448' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1245301")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1245301' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1245148")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1245148' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1278429")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1278429' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1235585")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1235585' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1284744")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1284744' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1245871")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1245871' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1231846")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1231846' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1220265")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1220265' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1220242")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1220242' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1268964")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1268964' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1272109")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1272109' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1267564")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1267564' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1291082")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1291082' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1266318")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1266318' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1266320")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1266320' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1240657")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1240657' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1231848")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1231848' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1249998")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1249998' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1267134")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1267134' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1249850")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1249850' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1279315")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1279315' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1267134")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1267134' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1279895")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1279895' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1258539")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1258539' + ',' + str(lat) + ',' + str(lon)
fhand = urllib.urlopen("http://fccinfo.com/CMDProASRLookup.php?tabSearchType=ASR+Search&sASR=1245147")
for line in fhand:
    if 'Structure Coordinates' in line:
        line = re.sub(' +',' ',line)
        latfull = line.split(' ')[2]
        lat = float(latfull.split('-')[0]) + float(latfull.split('-')[1])/60.0 + float(latfull.split('-')[2])/3600.0
        lonfull = line.split(' ')[4]
        lon = float(lonfull.split('-')[0]) + float(lonfull.split('-')[1])/60.0 + float(lonfull.split('-')[2])/3600.0
        print '1245147' + ',' + str(lat) + ',' + str(lon)
