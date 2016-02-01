#-*-coding:utf8-*-
import requests
import re
# url = 'https://www.crowdfunder.com/browse/deals'
url = 'https://www.crowdfunder.com/browse/deals&template=false'


# html = requests.get(url).text
# print html


#注意这里的page后面跟的数字需要放到引号里面。
data = {
    'entities_only':'true',
    'page':'2'
}
head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'}
html_post = requests.post(url,data=data, headers=head)

title = re.findall('"card-title">(.*?)</div>',html_post.text,re.S)
for each in title:
    print each