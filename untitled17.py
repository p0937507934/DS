# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 13:50:32 2021

@author: HSIPL39
"""

def swap(a,b):
    temp = a
    a = b
    b = temp
    print(id(a))
    print(id(b))
    return a,b

a = 1
b = 2
print(id(a))
print(id(b))
swap(a,b)
print(id(a))
print(id(b))

