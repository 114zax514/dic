import urllib2
from bs4 import BeautifulSoup

html = urllib2.urlopen("http://www.sasase.ics.keio.ac.jp/")

soup = BeautifulSoup(html)

print soup
