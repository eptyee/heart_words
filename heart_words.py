# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:59:37 2018

@author: skyligo
"""
import time
words= input('plz input the words:')
for item in words.split():
    print('\n'.join([''.join([(item[(x-y)%len(item)] if ((((x*0.05)**2+(y*0.1)**2-1)**3)-((x*0.05)**2)*(y*0.1)**3) <= 0 else ' ')for x in range(-30,30)]) for y in range(15,-15,-1)]))
    time.sleep(1)
for item in words.split():
    print('\n'.join([''.join([(item[(x-y)%len(item)] if ((((x*0.05)**2+(y*0.1)**2-1)**31)-((x*0.05)**2)*(y*0.1)**31) <= 0 else ' ')for x in range(-30,30)]) for y in range(15,-15,-1)]))
    time.sleep(1)
for item in words.split():
    print('\n'.join([''.join([(item[(x-y)%len(item)] if ((((x*0.05)**2+(y*0.1)**2-1)**51)-((x*0.05)**2)*(y*0.1)**51) <= 0 else ' ')for x in range(-30,30)]) for y in range(15,-15,-1)]))
    time.sleep(1)