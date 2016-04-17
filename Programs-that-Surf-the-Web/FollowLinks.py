#Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html 
#Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
#Last name in sequence: Anayah
#Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Kenan.html 
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: C

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
