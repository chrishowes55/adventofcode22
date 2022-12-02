#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:29:27 2022

@author: chris
"""


#part 1
def topcalories(path):
    file = open(path, 'r')
    cals = file.readlines()
    
    total = 0
    totals = []
    for i in cals:
        i = i.strip()
        print(i)
        if i == '':
            print(total)
            totals.append(total)
            total = 0
            continue
        total += int(i)
    totals.append(total)
        
    return totals

#part 2
def topthreecalories(totals):
    totals.sort(reverse=True)
    return totals[0]+totals[1]+totals[2]
        
    
    
tots = topcalories('input.txt')
print(topthreecalories(tots))
