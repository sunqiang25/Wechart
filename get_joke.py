# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import MySQLdb
import time,requests

timeout=5
host = 'http://www.qiushibaike.com'
#target = 'text'
target = "pic"
min_laugh_num = 500
min_joke_num = 10
# DB setting
username = 'root'
password = 'sq416221@'
dbname = 'test'

def get_html(url,timeout=None):
    # 获取指定url的html源码
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  }
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request,timeout=timeout)
    except urllib2.HTTPError,e:
        time.sleep(2)
        print e
        raise Exception,'[Error] 遇到HTTP 503 错误，程序休眠了一下……'
    except Exception,e:
        raise Exception,'[Error] get_html()获取源码失败\n%s'%e
    return response.read().decode("utf-8")

def getPagesum():
    # get total page number
    try:
        url = '%s/%s'%(host,target)
        html = get_html(url,timeout)
        pattern = re.compile(r'<span class="page-numbers">(.*?)</span>',re.S)
        items = re.findall(pattern,html) #list
        print items
    except Exception,e:
        raise Exception,'[Error] getPagesum()获取总页数失败\n%s'%e
    return int(items[-1])
print getPagesum()

def get_jokes():
    print 'start getting...'
    try:
        pagesum = getPagesum()
    except Exception,e:
        print e
        return []
    joke_list = []
    for page in range(1,pagesum+1):
        print 'current page',page
        url = '%s/%s/page/%d/'%(host,target,page)
        html = get_html(url,timeout)
        #print html
        #print url
        pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?</div>(.*?)<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>',re.S)
        items = re.findall(pattern,html)
        #print items
        #print len(items)

        for item in items:
            print item[1].encode("utf-8")
            joke = {}
            joke['username'] = item[0].strip().encode("utf-8")
            joke["content"] = item[1].strip().encode('utf-8')
            temp = re.findall('<img.*?src="(.*?)".*?',item[2])
            joke['imgurl'] =temp[0].encode("utf-8")
            #if joke['imgurl']==0:
                #joke['imgurl']=''
            joke['laugh_num'] = int(item[3].strip())
            joke['comment_num']= int(item[4].strip())
            info = '用户名：%s\n内容：\n%s\n图片地址：%s\n好笑数：%d\n评论数：%d\n'%\
                   ( joke['username'] , joke['content'] , joke['imgurl'] , joke['laugh_num'] , joke['comment_num'] )
            if joke['imgurl']!='' and joke['laugh_num'] > min_laugh_num:
                print len(joke_list)
                print info
                joke_list.append(joke)

    return joke_list

def connectMySQL():
    # 连接mysql数据库
    conn = MySQLdb.connect(
        host='localhost',        
        user=username,
        passwd=password,
        db=dbname,
        )
    return conn

def save2mysql(joke_list):
    # 将抓取的段子存入数据库
    conn = connectMySQL()
    cur = conn.cursor()
    for i,joke in enumerate(joke_list):
        print '正在插入第%d条段子……'%(i+1)
        sql = 'select 1 from qiushi_joke where content = "%s" limit 1; '%(joke['content'])
        isExist = cur.execute(sql)
        if isExist==1:
            print '-> 该段子已存在于数据库！放弃插入！'
        else:
            sql = 'insert into qiushi_joke (username,content,laugh_num,comment_num,imgurl) values ("%s","%s","%d","%d","%s")'% ( joke['username'] , joke['content'] , joke['laugh_num'] , joke['comment_num'] , joke['imgurl'] )
            cur.execute(sql)
    print '正在提交以上所有操作……'
    conn.commit()

    cur.close()
    conn.close()

def main():
    #  主程序
    try:
        while True:
            joke_list = get_jokes()
            if len(joke_list)>=min_joke_num:   # 抓取到至少min_joke_num条笑话才行
                break
            time.sleep(2)
        save2mysql(joke_list)
    except Exception,e:
        print e

if __name__=='__main__':
    main()
#print get_html("http://www.qiushibaike.com/text/page/6/",timeout=5)
