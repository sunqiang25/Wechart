#coding=utf-8
from werobot import WeRoBot
import re,requests

robot = WeRoBot(enable_session=False,
    token='321324199008051296',
    APP_ID='wxb55200b80d315307',
    APP_SECRET='22f41eed8ac630f827de67d771438705')
'''
@robot.handler
def hello(message):
    return 'I Love Qiuju'
'''

@robot.text
def echo(message):
    msg = message.content.strip().encode("utf8")
    if re.compile(".*?joke.*?").match(msg):
        html = requests.get("http://39.106.189.163/joke/")
        content = html.text
        pattern = re.compile('<td class="content">(.*?)</td>.*?<img src="(.*?)".*?>',re.S)
        joke_content = re.findall(pattern,content)[0][0].encode("utf8")
        img_url = re.findall(pattern,content)[0][1].encode("utf8")
        #img ="<image src='%s'></image>"%img_url
        return "%s\n%s"%(joke_content,img_url)
@robot.key_click("music")
def music(message):
    return "You click the button of 'Love Music'"

