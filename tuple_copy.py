# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:17:09 2020

@author: Rahul
"""
list=[]
limit=int(input('Enter the no of values to be added:'))
for i in range(0,limit):
    ele=int(input())
    list.append(ele)
tupl=tuple(list) 
print(tupl)
list1=[]
n=int(input('Enter the number to be copied:'))
for i in range(0,n):
    print("Enter the number to be copied:")
    ele1=int(input())
    list1.append(ele1)
tuple_new=tuple(list1)    
print(tuple_new)
    
