#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:39:28 2022

@author: fost
convert ascii to binary 
"""
def binary_convert():
    d = input('Enter any ASCII/Unicode text to convert to binary:')
    c = ' '.join('{0:08b}'.format(ord(x), 'b') for x in d)
           
    print(c)
    
   
binary_convert()
