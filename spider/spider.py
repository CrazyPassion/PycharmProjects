#-*-coding:utf-8-*-

import requests

html = requests.get('http://tieba.baidu.com/f?ie=utf-8&kw=python')
html = requests.get('https://www.baidu.com')
print html.content