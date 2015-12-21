import urllib
import json

url_in = raw_input("Enter site here: ")
html = urllib.urlopen(url_in).read()

print html

info = json.loads(html)

s = 0
for v in info["comments"]:
    s = s + int(v["count"])
print s
