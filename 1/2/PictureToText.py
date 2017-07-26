#coding=utf-8

import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

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

    
def numbers_to_strings1():
    return  unicode("蛤",'UTF-8')

def readPicture():
    im = Image.open('6.jpg')

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
            pos = i+2 #16号字长度16，20 
            fill = img_array[j*theImageWide+i]
            text = numbers_to_strings1()
            draw.text((pos*large, j*large), text, font = font, fill=fill )
    
    NewImage.save('test2.jpg', 'jpeg');
    
if __name__=='__main__':   
    #main()
    #InputYourMessage()
    #for i in range(4):
    #    print i
    #print 5/4
    readPicture()