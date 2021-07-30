# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:54:35 2020

@author: Rahul
"""

list=[]
list1=[]
limit=int(input('Enter the no of values to be added:'))
for i in range(0,limit):
    ele=int(input())
    list.append(ele)
for i in list:
    if(i%5==0):
       list1.append(i)
print(list1)       
        
    