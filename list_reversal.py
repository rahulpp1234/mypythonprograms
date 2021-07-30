# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:30:09 2020

@author: Rahul
"""

list=[]
list_rev=[]
n=int(input('Enter the no of values to be added:'))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list) 
k=len(list)
for k in range(1,k+1):
    list_rev.append(list[-k])
print(list_rev)    
    

