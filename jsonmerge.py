#!../venv/bin/python
#coding:utf8

import sys,json,io,glob

#get all files with a name

if len(sys.argv) == 1:
  print 'file pattern'
  sys.exit()

pattern=sys.argv[1]

if len(sys.argv) == 3:
  outfile = sys.argv[2]
else:
  outfile = 'output.json'

output = []

filelist = glob.glob(pattern)

#filelist = ['prompts/daredevilkink_prompts-014.html', 'prompts/daredevilkink_prompts-001.html']


for filename in filelist:
    print filename
    with open(filename) as file:
      contents = json.loads(file.read())
      print 'file has',len(contents),'items'
      output.extend(contents)
    
print 'output has',len(output),'items'
with io.open(outfile, 'w', encoding='utf8') as json_file:
    data = json.dumps(output, ensure_ascii=False,encoding='utf8')
    # unicode(data) auto-decodes data to unicode if str
    json_file.write(unicode(data))