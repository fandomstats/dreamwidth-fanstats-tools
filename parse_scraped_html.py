#!../venv/bin/python
#coding:utf8

from lxml import html
import sys
import csv,io,json,glob
from BeautifulSoup import UnicodeDammit


if len(sys.argv) == 1:
  print 'missing folder name'
  sys.exit()

folder=sys.argv[1]

csvoutput = open(folder+".csv",'w')
promptlist = []
fieldnames=['title','url','date','note','replycount']
csvwriter = csv.DictWriter(csvoutput,fieldnames=fieldnames)

filelist = glob.glob(folder+"/*")
#print filelist

#filelist = ['prompts/daredevilkink_prompts-014.html', 'prompts/daredevilkink_prompts-001.html']


for filename in filelist:
  raw = open(filename)
  src = raw.read()
  raw.close()
  ud = UnicodeDammit(src, isHTML=True)
  tree = html.fromstring(ud.unicode.encode('utf-8'))
  items = tree.find_class('comment-depth-1')
  for n,item in enumerate(items):
    #prompt title
    #prompt url
    #note  
    title = item.cssselect('.comment-title span')
    if len(title) > 0:
      title = title[0]
      titletext = title.text_content().encode('utf-8')
      
      note = item.cssselect('.comment-content')
      if len(note) > 0:
	notetext = note[0].text_content().encode('utf-8')
      else:
	notetext = ''
	
      url = item.cssselect(".commentpermalink a")
      if len(url) > 0:
	urltext = url[0].get("href").encode('utf-8')
	
      
      date = item.cssselect(".datetime")
      if len(date) > 0:
	datetext = date[0].text_content().encode('utf-8')
      
      reply = item.cssselect(".expand a")
      if len(reply) > 0:
	replytext = reply[0].text_content().encode('utf-8')
	numbers = [int(s) for s in replytext.split() if s.isdigit()]
	if len(numbers) > 0:
	  replycount = numbers[0]
      
      prompt = {
	'title':titletext,
	'url':urltext,
	'note':notetext,
	'date':datetext,
	'replycount':replycount,
	}
      print prompt['date'] +': ' + str(prompt['replycount'])
      promptlist.append(prompt.copy())
      csvwriter.writerow(prompt)   
      
with io.open(folder+'.json', 'w', encoding='utf8') as json_file:
    data = json.dumps(promptlist, ensure_ascii=False,encoding='utf8')
    # unicode(data) auto-decodes data to unicode if str
    json_file.write(unicode(data))