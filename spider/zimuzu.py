#-*-coding:utf-8-*-

import requests
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def checkin(url):
    pass

def login(url):
    head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'}
    data = {
        'account':'von.king2010@gmail.com',
        'password':'357951jjey',
        'remember':'1',
        'url_back':'http://www.zimuzu.tv/user/user/'
    }
    html = requests.post(url, data= data,headers = head)
    # html = requests.get(data['url_back'])
    print type(html)

if __name__ == '__main__':
    loginurl = 'http://www.zimuzu.tv/User/Login/ajaxLogin'
    checkinurl = ''
    print "start check in zimuzu."

    # loginurl = 'http://www.jikexueyuan.com/'
    login(loginurl)
    # res = checkin(checkinurl)
    # if res != 200:
    #     print 'check in fail.'
    # else:
    #     print 'check in success.'
