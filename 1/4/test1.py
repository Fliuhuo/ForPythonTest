#coding=utf-8

import numpy as np
from numpy import cross, pi, sin ,cos, sqrt


from Tkinter import *  
  
def moveImage(event):#图片logo.gif的移动要绑定的函数  
    if event.keysym=='Up':  
        canvas.move(1,0,-3)#移动ID为1的事物，使得横坐标加0，纵坐标减3  
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
        canvas.itemconfig(pg,fill='blue')#填充ID为pg的事物，填充为blue  
      
  
def foo(app):  
    app.wm_maxsize(400,400)  
    canvas=Canvas(app,width=400,height=400)  
    canvas.pack()  
    im=PhotoImage(file='logo.gif')  
    
    
    
    canvas.create_image(200,200,image=im)  
    
    
    #tk=Tk()#窗口  
    #canvas=Canvas(tk,width=400,height=400)#画布  
    #canvas.pack()#显示出来  
    #myImage=PhotoImage(file='logo.gif')#图片格式必须为gif格式  
    
    theIm=canvas.create_image(0,0,anchor=NW,image=im)#加载图片  
    pg=canvas.create_polygon(10,10,10,60,50,35,fill='red')#创建三角形  
    #print (im);print (pg)  #显示图片和三角形的ID  
    canvas.bind_all('<KeyPress-Up>',moveImage)#绑定方向键 up  
    canvas.bind_all('<KeyPress-Down>',moveImage)  
    canvas.bind_all('<KeyPress-Left>',moveImage)  
    canvas.bind_all('<KeyPress-Right>',moveImage)  
    canvas.bind_all('<KeyPress-Up>',changeColor)  
    
    app.mainloop()  
    
  
app=Tk()  
foo(app)  



  
 
  
