#!/usr/bin/env python3 
print("Content-Type: text/html")
print()
import cgi, os
files = os.listdir('data')
listStr = ''
#'data'아래에 있는 파일을 for문을 사용해서 계속해서 가져옴
for item in files:
  listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId,'r').read()

else:
    pageId = '메인화면'
    description = '메인을 설명하는 본문입니다'
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">메인화면</a></h1>
  <ol>
      {listStr}
  </ol>
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc =description, listStr=listStr))
