import urllib
import xml.etree.ElementTree as ET

#http://python-data.dr-chuck.net/comments_264797.xml

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    url = urllib.urlopen(address)
    print 'Retrieving', address
    data = url.read()
    print 'Retrieved',len(data),'characters'
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    x=0
    sum=0
    for count in counts:
        x=x+1
        sum=sum+int(count.text)
    print x
    print sum
