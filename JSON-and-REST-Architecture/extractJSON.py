import json
import urllib

#http://python-data.dr-chuck.net/comments_264801.json
input = raw_input("Enter location: ")

print 'Retrieving', input
uh = urllib.urlopen(input)
data = uh.read()
print 'Retrieved',len(data),'characters'
info = json.loads(str(data))
print 'Count:', len(info)

sum=0
js=info["comments"]
for item in js:
    sum=sum+int(item["count"])
print sum
