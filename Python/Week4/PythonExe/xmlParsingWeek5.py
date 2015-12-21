import urllib
import xml.etree.ElementTree as ET



url = raw_input("Enter location: ")
tree = ET.fromstring(urllib.urlopen(url).read())
print tree
counts = tree.findall('.//comment')
s = 0
for item in counts:
    s = s + int(item.find('count').text)
print s
