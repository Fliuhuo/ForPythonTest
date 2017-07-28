#coding=utf-8

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import requests
import Queue
import urllib
import urllib2  
import re
import random
import time
from time import sleep
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def getTime():
    nowtime = time.localtime(time.time())
    return nowtime.tm_mon,nowtime.tm_mday

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
    
def getMatchSomeThing():
    #print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
    print(re.match('www', 'www.runoob.com'))
    print(re.match('com', 'www.runoob.com'))  


def test():

    url = 'http://www.itwhy.org'
    
    r = requests.get(url)    # 最基本的GET请求
    print(r.status_code)    # 获取返回状态
    t = requests.post(url, data={'comment': '测试POST'})   #带参数的GET请求
    print(r.url)
    print(t.text)


def store(url):
    print url

def test1():
    initial_page = "http://bangumi.bilibili.com/moe/2017/jp/index#/schedule?id=20170724"

    url_queue = Queue.Queue()
    seen = set()

    seen.add(initial_page)
    url_queue.put(initial_page)

    while(True): #一直进行直到海枯石烂
        if url_queue.qsize()>0:
            current_url = url_queue.get()    #拿出队例中第一个的url
            store(current_url)               #把这个url代表的网页存储好
            for next_url in extract_urls(current_url): #提取把这个url里链向的url
                if next_url not in seen:      
                    seen.put(next_url)
                    url_queue.put(next_url)
        else:
            break


def test2():
    
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    response = urllib2.urlopen('http://bangumi.bilibili.com/moe/2017/jp/index#/schedule?id=20170724')  
    html = response.read()  
    print html 

def InputYourMessage():
    theId = input("please enter your Id:")
    password = input("please enter your password:")
    print theId
    print password
    
    

    
if __name__=='__main__':   

    #print getTime()
    getMatchSomeThing()
    #url = 'http://bangumi.bilibili.com/moe/2017/jp/index#/schedule?id=20170728'
    #print getHtml(url)