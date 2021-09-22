# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 11:13:28 2021

@author: Mainak
"""

list=[]

#number of elements to be inputted
n=int(input("Enter the number of elements:"))

#iterating till range
for i in range(0,n):
    ele=int(input())
 
    list.append(ele)

print("Output : [",end='')
for number in list:
    if number>0:
        print(number,end=' ')
print("]")
    