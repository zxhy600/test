# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 16:49:49 2018

@author: wei
"""

from PIL import Image,ImageFont,ImageDraw,ImageColor


def img_addnum(img,num):
    img1=Image.open("test1.jpg") # 打开图片
    draw1= ImageDraw.Draw(img1) # 画
    font1= ImageFont.truetype("arial.ttf",size=60) #字体
    color1=ImageColor.getcolor("red","RGB") #颜色
    w,h=img1.size
    draw1.text((w*0.9,h*0.05),num,fill=color1,font=font1) # 内容
    
    img1.save("img_addnum.jpg","jpeg") #保存
    
    return 0

    

if __name__ == '__main__':
    img_addnum("test0.jpg","68")
    

    
   
    
