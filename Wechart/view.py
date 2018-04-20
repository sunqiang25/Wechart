#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
import MySQLdb
import random
import json


username = 'root'      
password = 'sq416221@'     
dbname = 'test'     

def connectMySQL():
    # 连接mysql数据库
    conn = MySQLdb.connect(
        host='localhost',

        user=username,
        passwd=password,
        db=dbname,
        )
    return conn

def get_joke(request):
    response = ''
    try:
        conn = connectMySQL()
        cur = conn.cursor()
        # 生成随机抓取id
        sql = 'select count(*) from qiushi_joke'
        cur.execute(sql)
        joke_sum = cur.fetchone()[0]
        joke_idx = random.randint(987,joke_sum+987)
       # print joke_idx
        # 抓取该id的段子数据
        sql = 'select * from qiushi_joke where id=%d'%joke_idx
        cur.execute(sql)
        #print cur.execute(sql)
        joke_list = []
        joke = {}
        joke['id'],joke['username'],joke['content'],joke['laugh_num'],joke['comment_num'],joke['imgurl'] = cur.fetchone()
        response = json.dumps(joke,ensure_ascii=False)
        joke_list.append(joke)
        print joke_list
        # 关闭数据库连接
        cur.close()
        conn.close()
    except Exception as e:
        print e
   # return HttpResponse(response)
    return render_to_response('joke.html',locals())
def get_video(request):
    response =''
    try:
        conn = connectMySQL()
        cur = conn.cursor()
        sql = 'select count(*) from neihan_video'
        cur.execute(sql)
        video_sum = cur.fetchone()[0]
        video_idx = random.randint(24,video_sum+17)
        #print video_sum
        #print video_idx
        sql = 'select * from neihan_video where id=%d'%video_idx
        cur.execute(sql)
        video_list = []
        video = {}
        video['id'],video['content'],video['video_url'],video['favorite_count']= cur.fetchone()
        response = json.dumps(video,ensure_ascii=False)
        video_list.append(video)
        #print video
        cur.close()
        conn.close()
    except Exception,e:
        print e
    return render_to_response('neihan_video.html',locals())
