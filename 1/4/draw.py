#coding=utf-8

import numpy as np
from numpy import cross, pi, sin ,cos, sqrt


import time  
from Tkinter import *
def moveImage(event):#ͼƬlogo.gif���ƶ�Ҫ�󶨵ĺ���  
    if event.keysym=='Up':  
        canvas.move(1,0,-3)#�ƶ�IDΪ1�����ʹ�ú������0���������3  
    elif event.keysym=='Down':  
        canvas.move(1,0,+3)  
    elif event.keysym=='Left':  
        canvas.move(1,-3,0)  
    elif event.keysym=='Right':  
        canvas.move(1,3,0)  
    tk.update()  
    time.sleep(0.05)  
      
def changeColor(event):  
    if event.keysym=='Up':  
        canvas.itemconfig(pg,fill='blue')#���IDΪpg��������Ϊblue  
      
tk=Tk()#����  
canvas=Canvas(tk,width=1000,height=1000)#����  
canvas.pack()#��ʾ����  
#myImage=PhotoImage(file='logo.gif')#ͼƬ��ʽ����Ϊgif��ʽ  
  
#im=canvas.create_image(0,0,anchor=NW,image=myImage)#����ͼƬ  
#pg=canvas.create_polygon(10,10,10,60,50,35,fill='red')#����������  
#print (im);print (pg)  #��ʾͼƬ�������ε�ID  
#canvas.bind_all('<KeyPress-Up>',moveImage)#�󶨷���� up  
#canvas.bind_all('<KeyPress-Down>',moveImage)  
#canvas.bind_all('<KeyPress-Left>',moveImage)  
#canvas.bind_all('<KeyPress-Right>',moveImage)  
  
#canvas.bind_all('<KeyPress-Up>',changeColor)  

tk.mainloop() 