# _*_ coding:utf-8 _*_
import os,sys,time,datetime
import re
import requests,json
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf8')
def get_video():
    current_time = time.time()
    #n = 0
    result_list =[]

    for i in range(int(current_time)-100000,int(current_time)-10000,1000):
        url = 'http://neihanshequ.com/video/?is_json=1&app_name=neihanshequ_web&max_time=%s'%i
        #print url
        data = requests.get(url).text.encode("utf8")
        hjson = json.loads(data)
    #print hjson['data']['data'][-1]['group']
        for temp in hjson['data']['data']:
            result_dist = {}
            favorite_count = temp['group']['favorite_count']
            if favorite_count > 5000:
                result_dist['favorite_count'] = favorite_count
                #result_dist['comment_count'] = temp['group']['comment_count']
                #result_dist['user_favorite'] = temp['group']['comment_count']
                result_dist['mp4_url'] = temp['group']['mp4_url']
                result_dist['content'] = temp['group']['content'].encode("utf8")
                if result_dist not in result_list:
                    result_list.append(result_dist)

                #print favorite_count
                #print 'comment_count',temp['group']['comment_count']
                #print 'user_favorite',temp['group']['user_favorite']
                #print 'content', temp['group']['content']
                #print temp['group']['mp4_url']
                #n+=1
                #print n
    return result_list
def connectMySQL():
    conn = MySQLdb.connect(host='localhost',user='root',passwd='sq416221@',db='test',charset='utf8',)
    return conn
def save2mysql(result_list):
    conn = connectMySQL()
    cur = conn.cursor()
    for i,video in enumerate(result_list):
        print '正在插入第%d条内涵视频'%(i+1)
        sql = 'select 1 from neihan_video where video_url="%s" limit 1;'%(video['mp4_url'])
        isExit = cur.execute(sql)
        if isExit == 1:
            print '数据库中已经存在此内涵视频，放弃插入'
        else:
            try:
                sql = 'insert into neihan_video(content,favorite_count,video_url) values ("%s","%s","%s")'%(video['content'],video['favorite_count'],video['mp4_url'])
                cur.execute(sql)
            except Exception,e:
                continue
    print '正在提交操作...'
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    try:
        result_list = get_video()
        save2mysql(result_list)
    except Exception,e:
        print e

''''
timeStamp=1515284348
d = datetime.datetime.fromtimestamp(timeStamp)
str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f")
print str1
current_time= time.time()
print int(current_time)
#print datetime.timestamp(current_time)
'''
