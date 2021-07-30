# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:08:17 2020

@author: Rahul
"""
list=[]
limit=int(input('Enter the no of values to be added:'))
for i in range(0,limit):
    ele=int(input())
    list.append(ele)
print(list) 
print('Largest Number: ', max(list))
