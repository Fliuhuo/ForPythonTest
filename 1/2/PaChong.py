#coding=utf-8

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import requests
import Queue
import urllib
import urllib2  
import re
import random
from time import sleep
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter





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
    
def numbers_to_strings(argument):
    switcher = {
        0: unicode("珂",'UTF-8'),
        1: unicode("朵",'UTF-8'),
        2: unicode("莉",'UTF-8'),
        3: unicode("哔",'UTF-8'),
        4: unicode("哩",'UTF-8'),
        5: unicode("哔",'UTF-8'),
        6: unicode("哩",'UTF-8'),
        7: unicode("萌",'UTF-8'),
        8: unicode("战",'UTF-8'),
        9: unicode("加",'UTF-8'),
        10: unicode("油",'UTF-8'),
    }
    return switcher.get(argument, "nothing")


def readPicture():
    im = Image.open('1.jpg')

    img_data=im.getdata()
    img_array = list(img_data)
    
    theAllImageLen = len(img_array)
    theImageWide = im.getbbox()[2]
    theImageLeath = im.getbbox()[3]
    
    print  theImageWide,theImageLeath # 134 ，187
    
    large = 20
    
    NewImage = Image.new( 'RGB', (theImageWide*large,theImageLeath*large),(192, 192, 192) )
    font = ImageFont.truetype('STXIHEI.TTF', 16)
    draw = ImageDraw.Draw(NewImage)
    
    for j in range(theImageLeath):
        for i in range(theImageWide):
            pos = i+2 #八号字长度8，10 
            fill = img_array[j*theImageWide+i]
            text = numbers_to_strings(i%11)
            draw.text((pos*large, j*large), text, font = font, fill=fill )
    
    NewImage.save('test3.jpg', 'jpeg');
    
    
def readPicture1():
    im = Image.open('1.jpg')

    img_data=im.getdata()
    img_array = list(img_data)
    
    theAllImageLen = len(img_array)
    theImageWide = im.getbbox()[2]
    theImageLeath = im.getbbox()[3]
    
    print  theImageWide,theImageLeath # 134 ，187
    
    large = 10
    
    NewImage = Image.new( 'RGB', (theImageWide*large,theImageLeath*large),(192, 192, 192) )
    font = ImageFont.truetype('STXIHEI.TTF', 16)
    draw = ImageDraw.Draw(NewImage)
    
    k = -1
    for j in range(theImageLeath):
        for i in range(theImageWide):
            k = k + 1
            if (i%2 == 0) and (j%2 == 0):
                pos = i+2 #八号字长度8，10 
                fill = img_array[j*(theImageWide)+i]
                text = numbers_to_strings(k%11)
                draw.text((pos*large, j*large), text, font = font, fill=fill )
            else:
                k = k - 1
                
                
    
    NewImage.save('test4.jpg', 'jpeg');
    
    
if __name__=='__main__':   
    #main()
    #InputYourMessage()
    #for i in range(4):
    #    print i
    #print 5/4
    readPicture1()