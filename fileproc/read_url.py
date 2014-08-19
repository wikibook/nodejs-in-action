import urllib
url = "http://www-personal.buseco.monash.edu.au/~hyndman/TSDL/ecology1/hopedale.dat"
web_page = urllib.urlopen(url)
for line in web_page:
    line = line.strip()
    print line
web_page.close()
