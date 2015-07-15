#!../venv/bin/python
#coding:utf8
import json, io 
from BeautifulSoup import UnicodeDammit

if len(sys.argv) > 4:
  print 'usage: deliciousfile.json dreamwidthfile.json outputname.json'
  sys.exit()

delicious = sys.argv[1]
dreamwidth = sys.argv[2]
outputname = sys.argv[3]

deliciousraw = open(delicious)
delicious = json.loads(deliciousraw.read())
deliciousraw.close()
commentsraw = open(dreamwidth)
comments = json.loads(commentsraw.read())
commentsraw.close()
delsort = sorted(delicious, key=lambda k: k['url']) 
comsort = sorted(comments, key=lambda k: k['url'])
#print str(len(delsort)) + " vs " + str(len(comsort())
#http://stackoverflow.com/questions/7327344/python-quickest-way-to-merge-dictionaries-based-on-key-match
print str(len(delsort)) + " vs " + str(len(comsort))

#comsort: url, note, replycount, date, title
#delsort: url, note, title, tags

promptlist = []

c=0 #do I need this?
d=0
url_d = ''
url_c = ''
dl = {}
com = {}
for n in range (0,len(comsort)-1):
  #if url_d == url_c, then merge the records, and move on to next com
  #if url_d != url_c, try the next index
  com = comsort[n]
  url_c = com['url']
  
  while (url_d != url_c and d < len(delsort)):
    dl = delsort[d]
    url_d = dl['url']
    d = d+1
    
  print url_c +' ' +url_d + ' = match'
  prompt  = {
    'url': url_c,
    'title': dl['title'],
    'date': com['date'],
    'note': com['note'],
    'replycount': com['replycount'],
    'tags': dl['tags']
  }
  promptlist.append(prompt.copy())

with io.open(outputname, 'w', encoding='utf8') as json_file:
    print 'final output:',len(promptlist),'items'
    data = json.dumps(promptlist, ensure_ascii=False,encoding='utf8')
    # unicode(data) auto-decodes data to unicode if str
    json_file.write(unicode(data))