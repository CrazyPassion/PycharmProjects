#-*_coding:utf8-*-
import requests
import re
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class spider(object):
    rootdir = 'pic'
    curdir = ' '
    def __init__(self):
        print u'开始爬取内容。。。'
        print self.rootdir + self.curdir

    def getsource(self,url):
        html = requests.get(url)
        return html.text

    def getalllinkincurrenthtml(self,source):
        alllinksource = re.findall('<dl class="list-left public-box">(.*?)</dl>', source, re.S)
        # print alllinksource[0].decode('gbk')
        alllinks = re.findall('<dd><a target="_blank" href="(.*?)"><img',alllinksource[0],re.S)
        # print alllinks
        return alllinks

    def getpagesnum(self,source):
        numres = re.findall(u'<div class="content-page">(.*?)</span><span',source,re.S)
        num = re.findall('<span class="page-ch">\xb9\xb2(.*?)\xd2\xb3',numres[0],re.S)
        print num[0]
        return num[0]

    def downloadpic(self,source,num):
        picsource = re.findall('<div class="content-pic"><a href=(.*?)/></a></div>',source,re.S)
        print 'picsource:'+picsource[0].decode('gbk')
        picaddr = re.findall(' src="(.*?)"', picsource[0], re.S)
        # print 'picaddr' + picaddr[0]
        pic = requests.get(picaddr[0])
        picfile = self.rootdir + '//' + self.curdir + '//' + str(num) + '.jpg'
        fp = open(picfile,'wb')
        fp.write(pic.content)
        fp.close()
        # return picsource

    def getfoldername(self,content):
        picsource = re.findall('<div class="content-pic"><a href=(.*?)/></a></div>',content,re.S)
        print picsource[0].decode('gbk')
        foldername = re.findall(r'alt="(.*?)\(', picsource[0].decode('gbk'), re.S)
        # print foldername
        # print type(foldername)
        print 'fnmae: '+ foldername[0]

        print 'floder name: '+foldername[0].decode('utf')
        return foldername[0]

    def saveonelink(self,link):
        pichtml = requests.get(link)
        num = self.getpagesnum(pichtml.content)
        self.curdir = self.getfoldername(pichtml.content).decode('utf8')
        # print self.curdir
        try:
            os.mkdir(os.path.join(self.rootdir, self.curdir))
        except OSError as e:
            if e.errno != 17:
                raise
            # else:
            #     return
        self.downloadpic(pichtml.content, 1)
        for i in range(2,int(num) + 1):
            currentpicnum = re.search('xinggan/(\d+)',link).group(1)
            reallink = currentpicnum + '_' + str(i)
            nextpiclink = re.sub('xinggan/\d+','xinggan/%s'%reallink,link,re.S)
            print "nextlink: " + nextpiclink
            nextpichtml = requests.get(nextpiclink)
            self.downloadpic(nextpichtml.content,i)

    def saveonepage(self,url):
        html = ssspider.getsource(url)
        alllinkinhtml = ssspider.getalllinkincurrenthtml(html)
        for link in alllinkinhtml:
            self.saveonelink(link)


if __name__ == '__main__':

    firsturl = 'http://www.mm131.com/xinggan/'
    ssspider = spider()
    try:
        os.mkdir(ssspider.rootdir)
    except OSError as e:
        if e.errno != 17:
            raise

    # ssspider.saveonepage(firsturl)
    print 'page: '+ '1 ' + 'done'
    securl ='http://www.mm131.com/xinggan/list_6_1.html'
    for page in range(41,61):
        nextcul = re.sub('list_6_\d+','list_6_%d'%page,securl,re.S)
        ssspider.saveonepage(nextcul)
        print 'page: '+ str(page) + ' done'


    # all_links = jikespider.changepage(url,20)
    # for link in all_links:
    #     print u'正在处理页面：' + link
    #     html = jikespider.getsource(link)
    #     everyclass = jikespider.geteveryclass(html)
    #     for each in everyclass:
    #         info = jikespider.getinfo(each)
    #         classinfo.append(info)
    # jikespider.saveinfo(classinfo)


