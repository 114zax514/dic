#coding:utf-8
import urllib2

print('調べたい単語')
word = raw_input('>> ')
fp = urllib2.urlopen('http://ejje.weblio.jp/content/'+word)
html = fp.read()
fp.close()

index = html.find('主な意味')
index2 = html.find('</td></tr></tbody></table></div>')
print(html[index+51:index2])
