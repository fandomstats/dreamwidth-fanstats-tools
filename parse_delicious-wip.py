#!../venv/bin/python
#coding:utf8

from lxml import html
import csv,io,json
from BeautifulSoup import UnicodeDammit

if len(sys.argv) > 2:
  print 'missing source filename'
  sys.exit()

rawname = sys.argv[1]

deliciousraw = open(delicious)
delicious = json.loads(deliciousraw.read())
deliciousraw.close()
commentsraw = open(dreamwidth)
comments = json.loads(commentsraw.read())
commentsraw.close()

raw = open(rawname)
src = raw.read()
raw.close()
csvoutput = open("delicious.csv",'w')
promptlist = []
fieldnames=['title','url','note','tags','other']
csvwriter = csv.DictWriter(csvoutput,fieldnames=fieldnames)

ud = UnicodeDammit(src, isHTML=True)
tree = html.fromstring(ud.unicode.encode('utf-8'))

items = tree.find_class('item')
for n,item in enumerate(items):
  #prompt title
  #prompt url
  #note
  #tags  
  title = item.cssselect('.title')
  if len(title) > 0:
    title = title[0]
    
    note = item.cssselect('.note')
    if len(note) > 0:
      notetext = note[0].text_content().encode('utf-8')
    else:
      notetext = ''
      
    tagelems = item.cssselect('.dropdown-menu')
    tags = []
    if len(tagelems) > 0:
      for tag in tagelems:
	tagtext = tag.get("data-tag")
	if tagtext is not None:
	  tags.append(tagtext)
      
    prompt = {
      'title':title.text_content().encode('utf-8'),
      'url':title.get("href").encode('utf-8'),
      'note':notetext,
      'tags':tags,
      }
    promptlist.append(prompt.copy())
    prompt['tags'] = ",".join(tags)
    prompt['tags'] = prompt['tags'].encode('utf-8')
    csvwriter.writerow(prompt)    
  
with io.open('delicious.json', 'w', encoding='utf8') as json_file:
    data = json.dumps(promptlist, ensure_ascii=False,encoding='utf8')
    # unicode(data) auto-decodes data to unicode if str
    json_file.write(unicode(data))