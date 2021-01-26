from __future__ import unicode_literals
from threading import Timer
from wxpy import *
from wechat_sender import Sender
import time,requests
import datetime
import threading

bot = Bot(console_qr=2,cache_path='botoo.pk1') # 把consol_qr=2去掉，二维码是当做图片弹出来，否则则是以像素的方式打印出来，后面的参数是热登录，
#bot = Bot()

def get_news():
    # 这里是把今日糍粑每日一句中拿过来的信息发送给你朋友
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['translation']
    return contents,translation


def send_news():
    try:
        my_friend = bot.friends()
        my_friend = bot.friends().search('CJ🐳')[0] # 朋友微信昵称（不是备注，不是微信账号）
        #my_friend = bot.friends().search('Joey')[0] # 朋友微信昵称（不是备注，不是微信账号）
        for i in range(101):
            my_friend.send('我爱你')
    except:
        my_friend = bot.friends().search('Joey')[0]  # 你的微信名称，不是微信号
        my_friend.send(u'消息发送失败')


if __name__ == '__main__':
    #now = datetime.datetime.now()
    #next_time = datetime.datetime(2021,1,1,0,0,0,0)
    #timer_start_time = (next_time - now).total_seconds()
    #timer = threading.Timer(timer_start_time, send_news)
    #timer.start()
    send_news()