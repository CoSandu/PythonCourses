import re

f = open(r'C:\Constantin\Corsi_Online\Python\regx.txt', 'r')

interi = []
tot = 0

for line in f:
    x = re.findall('[0-9]+', line)
    if x:
        interi.append(x)

for val in interi:
    for v in val:
        tot = int(v) + tot

print tot
f.close()
