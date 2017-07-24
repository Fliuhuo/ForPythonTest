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
from PIL import Image
#from skimage import io

def main():
    url='http://bangumi.bilibili.com/moe/2017/jp/index#/schedule?id=20170724'    #感觉这个话题下面美女多    
    headers={}
    i=1
    for x in xrange(20,3600,20):        
        data={'start':'0','offset':str(x),'_xsrf':'a128464ef225a69348cef94c38f4e428'}        #知乎用offset控制加载的个数，每次响应加载20        
        content=requests.post(url,headers=headers,data=data,timeout=10).text        #用post提交form data
        print "content is"
        print content
        imgs=re.findall('<img src=\\\\\"(.*?)_m.jpg',content)          #在爬下来的json上用正则提取图片地址，去掉_m为大图          
        for img in imgs:            
            try:
                img=img.replace('\\','')                #去掉\字符这个干扰成分                
                pic=img+'.jpg'
                path='D:\\myWork\\ForPythonTest\\1\\2\\jpg\\'+str(i)+'.jpg'                #声明存储地址及图片名称                
                urllib.urlretrieve(pic,path)                #下载图片                
                print u'下载了第'+str(i)+u'张图片'
                i+=1                
                sleep(random.uniform(0.5,1))                #睡眠函数用于防止爬取过快被封IP               
            except:
                print u'抓漏1张'                
                pass
        sleep(random.uniform(0.5,1))

def test():
    #url='http://bangumi.bilibili.com/moe/2017/jp/index#/schedule?id=20170724'       
    #headers={}
    #data = {}
    #content = requests.post(url,headers,data,timeout = 10).text
    #print content

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


def readPicture():
    im = Image.open('picture.jpg')
    #im.show()
    
    r,g,b = im.split()#分割成三个通道 
    print r,g,b
    #r.show()  
    #g.show()  
    #b.show()  
    im = Image.merge("RGB", (g, b, r))#将b,g,r 三个通道进行翻转。
    im.show()
    
    #img=io.imread('picture.jpg')
    #io.imshow(img)
    #picture = mpimg.imread('picture.jpg') # 读取和代码处于同一目录下的 lena.png
    # 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
    #picture.shape #(512, 512, 3)

    #plt.imshow(picture) # 显示图片
    #plt.axis('off') # 不显示坐标轴
    #plt.show()    


    
    
if __name__=='__main__':   
    #main()
    #InputYourMessage()
    readPicture()
