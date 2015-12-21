import re

i = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'

s = re.findall('href=".+"', i)

print s
