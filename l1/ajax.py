# -*- coding: utf8 -*-
__author__ = 'vonking'
import urllib
import urllib2
import json
'''
poiName = "上海世博"
postdata = urllib.urlencode({
    'keyWords':poiName,
    'searchType':'1'
})
req = urllib2.Request(
url=' http://www.sgs.gov.cn/lz/etpsInfo.do?method=doSearch',
data=postdata
)
data= urllib2.urlopen(req).read()
print data'''


if __name__ == "__main__":
    d = '{"pageIndex":0,"pageSize":30,"title":""}'
    request = urllib2.Request('http://bbs.csdn.net/topics/350211361', d)
    request.add_header("Content-Type", "application/json; charset=utf-8")
    print request.headers
    f = urllib2.urlopen(request)
    rss_content = f.read()
    content = rss_content.decode("gbk")
    content = json.loads(content)


'''def request_ajax_data(url,data,referer=None,**headers):
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    req.add_header('X-Requested-With','XMLHttpRequest')
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116')
    if referer:
        req.add_header('Referer',referer)
    if headers:
        for k in headers.keys():
            req.add_header(k,headers[k])

    params = urllib.urlencode(data)
    response = urllib2.urlopen(req, params)
    jsonText = response.read()
    return json.loads(jsonText)



ajaxRequestBody = {"blogId":blogId,"postId":entryId,"blogApp":blogApp,"blogUserGuid":blogUserId}
ajaxResponse = request_ajax_url('http://outofmemory.cn/fakeAjax',ajaxRequestBody)'''