#coding:utf-8
import urllib2
import sys
i = True 
while i: 
    print('調べたい単語(exitで終了)')
    word = raw_input('>> ')
    if(word == 'exit'):
        sys.exit()
    fp = urllib2.urlopen('http://ejje.weblio.jp/content/'+word)
    html = fp.read()
    fp.close()

    index = html.find('主な意味')
    index2 = html.find('</td></tr></tbody></table></div>')
    print(html[index+51:index2])
