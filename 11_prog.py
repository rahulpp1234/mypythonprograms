# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 00:43:34 2020

@author: Rahul
"""

list=[]
limit=int(input('Enter the no of values to be added:'))
for i in range(0,limit):
    ele=int(input())
    list.append(ele)
print('Largest Number: ',max(list))