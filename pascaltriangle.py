# -*- coding: utf-8 -*-
"""
Created on Sun May 29 17:17:22 2022

@author: shabdar
"""

def pascaltriangle(n):
    list1=[]
    for i in range(n):
        list1.append([1]*(i+1))
        print (list1)
        
    for i in range(2,n):  
        for j in range(1,i)  :
            list1[i][j]=list1[i-1][j-1]+list1[i-1][j]
    return list1        
num=int(input("Enter Number: "))
x=pascaltriangle(num)
for i in x:
    print(i)