import urllib

f = urllib.urlopen('http://www.ithacaweb.org/')

conta = dict()
for line in f:
    parole = line.split()
    for parola in parole:
        conta[parola] = conta.get(parola, 0) + 1
print conta
