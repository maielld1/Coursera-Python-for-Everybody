import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
count=0
sum=0
for tag in tags:
    # Look at the parts of a tag
    count=count+1
    sum=sum+int(tag.string)
print "Count", count
print "Sum", sum
