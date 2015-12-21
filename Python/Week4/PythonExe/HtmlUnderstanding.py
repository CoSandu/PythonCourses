import urllib
from BeautifulSoup import *


url = raw_input("Enter - ")
count = 4
position = 18

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)


#till here looks at contents

# tags = soup("span")
# s = 0
# for tag in tags:
#     s = s + int(tag.contents[0])
#
# print s


#now looks at sites

tags = soup("a")


def leggi_nomi(url_in):
    html = urllib.urlopen(url_in).read()
    soup = BeautifulSoup(html)
    tags = soup("a")
    url = tags[position-1].get("href")
    return url

a = leggi_nomi(url)
print a
b = leggi_nomi(a)
print b
c = leggi_nomi(b)
print c
d = leggi_nomi(c)
print d
f = leggi_nomi(d)
print f
g = leggi_nomi(f)
print g
h = leggi_nomi(g)
print h
