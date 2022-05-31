# -*- coding: utf-8 -*-
"""
Created on Tue May 31 09:57:07 2022

@author: shabdar
"""
n=int(input("تعداد ضلع آخرین چندضلعی :  "))
import turtle
turtle.speed(0)
c=20
#turtle.penup()
e=-10
f=-8.66
turtle.penup()
turtle.goto(e,f)
turtle.pendown()
#turtle.
for i in range(3,n+1):
    d=360/i
    c+=10 
    e=-c/2
    f=-(8.66)*(((2**(1/2))*(i-3))/((2**(1/2))))
    turtle.penup()
    turtle.goto(e,f)
    turtle.pendown()
    # if i%2!=0:
    #     turtle.left(25)
        
    for j in range(0,i):
       
            #turtle.left(d)
            turtle.forward(c) 
            turtle.left(d)
      
        
    
    