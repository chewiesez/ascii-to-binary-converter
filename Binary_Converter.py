#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:39:28 2022

@author: fost
python challenge 3 convert a decimal to binary 
"""
def binary_convert():
    d = str(input('Enter a decimal number to convert:'))
    c = ' '.join('{0:08b}'.format(ord(x), 'b') for x in d)
           
    print(c)
    
   
binary_convert()
