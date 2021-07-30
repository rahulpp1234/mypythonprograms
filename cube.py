# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 14:27:27 2020

@author: Rahul
"""

def fun(num):
    cube=0
    for i in range(0,num):
        cube=cube+i**3
    print(cube)
n=int(input("Enter your number :"))   
fun(n) 
    

