import urllib2
from bs4  import BeautifulSoup

html = urllib2.urlopen("http://pente.koro-pokemon.com/data/speed-list.shtml")
soup = BeautifulSoup(html)

result = soup.find_all(class_="th2")
print len(result)
