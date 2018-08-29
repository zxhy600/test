# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 16:49:49 2018

@author: wei
"""

from PIL import Image,ImageFont,ImageDraw,ImageColor


def img_addnum(img,num):
    img1=Image.open("test1.jpg")
    draw1= ImageDraw.Draw(img1)
    font1= ImageFont.truetype("arial.ttf",size=60)
    color1=ImageColor.getcolor("red","RGB")
    w,h=img1.size
    draw1.text((w*0.9,h*0.05),num,fill=color1,font=font1)
    
    img1.save("img_addnum.jpg","jpeg")
    
    return 0

    



img_addnum("test1.jpg","68")
    

    
   
    