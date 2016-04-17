import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: '))
x=0
n=0

while n<count:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    for link in tags:
        x=x+1
        if x==pos:
            url=link.get('href',None)
            print "Retrieving:", url
            x=0
            break
    n=n+1
