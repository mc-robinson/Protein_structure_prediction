# -*- coding: utf-8 -*-
"""
Created: Tue Jun 28 13:46:48 2016
Author: matthewrobinson (Python 3.5)

Description:
"""
import numpy as np
import matplotlib.pyplot as plt

file_name = "alignment_stats_9-5-2016"

import os
dirList = os.listdir(file_name)

folders = np.array(dirList)


mypath = "/Users/matthewrobinson/Documents/spyder/scratch/alignment_stats_9-5-2016/"

import glob
newList = glob.glob('./alignment_stats_9-5-2016/*.txt') #had to change this since no folders now

fileArr = np.array(newList)

dt = np.dtype((str, 2000))   # 35-character string
mapping = np.empty((fileArr.size,3),dt)

count = 0
for file in fileArr:
    temp_arr = np.loadtxt(file)
    
    if temp_arr.size > 0:
        temp_string = file.split("/")[2]
        second = str(temp_arr[1])
        seven = str(temp_arr[7])
    
        mapping[count,0] = temp_string
        mapping[count,1] = second
        mapping[count,2] = seven
    
    count = count + 1
    



#count = 0
#for file in fileArr:
#    temp_arr = np.loadtxt(file)
#    finalList[count][0] = folders[count]
#    finalList[count][1] = temp_arr[1]
#    finalList[count][2] = temp_arr[-2]
#    count = count + 1


#count = 0
#for folder in folders:
#    temp_str = mypath + folders[count] + "/"
#    if not temp_str.endswith(".tar"):
#        fileArr[count] = os.listdir(temp_str)
#    count = count + 1
