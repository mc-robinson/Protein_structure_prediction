# -*- coding: utf-8 -*-
"""
Created: Thu Jul 28 16:25:38 2016
Author: matthewrobinson (Python 3.5)

Description: Code to parse the FINDSITE metal output
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import csv

#dir_name = "LOMETS_test_output"
#
#import os
#dirList = os.listdir(dir_name)
#folders = np.array(dirList)

mypath = "/Users/matthewrobinson/Documents/spyder/scratch/FINDSITE_output_files/" #unnecessary I think
import glob
newList = glob.glob('./FINDSITE_output_files/*/*.dat') #might have to change this
fileArr = np.array(newList)

metal_dict = dict({})
res_dict = dict({})
rkpt_dict = dict({})

for file in fileArr:

    file_name = re.split("./FINDSITE_output_files/",file)[1]
    file_name = re.split("/",file_name)[0]
    print(file_name)
    
    temp_df = pd.read_table(file)
    dt = np.dtype((str, 2000))
    temp_arr = np.array(temp_df.values,dt)
    
    metal_list = []
    res_list = []
    rkpt_list = []
    
    for i in range(0,temp_arr.size-1):
        if ("METAL" in temp_arr[i,0]):
            metal_str_list = re.split(' +',temp_arr[i,0])
            if float(metal_str_list[2]) > 0.0:
                metal_list.append(metal_str_list)
        if ("RESIDUE" in temp_arr[i,0]):
            res_str_list = re.split(' +',temp_arr[i,0])
            res_list.append(res_str_list)
            if res_str_list[2] == 'R' or res_str_list[2] == 'K' or res_str_list[2] == 'P' or res_str_list[2] == 'T':
                rkpt_list.append(res_str_list)
                
    metal_dict[file_name] = metal_list
    res_dict[file_name] = res_list
    rkpt_dict[file_name] = rkpt_list
    
output_path = "/Users/matthewrobinson/Documents/spyder/scratch/FINDSITE_data/" 
for key in metal_dict:
    file_string = output_path + key + "_metals.txt"
    f_output = open(str(file_string), 'w')
    
    for row in metal_dict[key]:
        for item in row:
            f_output.write("%s\t" % item)
        f_output.write("\n")
    f_output.close() 

for key in res_dict:
    file_string = output_path + key + "_residues.txt"
    f_output = open(str(file_string), 'w')
    
    for row in res_dict[key]:
        for item in row:
            f_output.write("%s\t" % item)
        f_output.write("\n")
    f_output.close()

for key in rkpt_dict:
    file_string = output_path + key + "_rkpt_residues.txt"
    f_output = open(str(file_string), 'w')
    
    for row in rkpt_dict[key]:
        for item in row:
            f_output.write("%s\t" % item)
        f_output.write("\n")
    f_output.close()
              
#figure out what we want to do about stars. It also throws the alignment off by a lot.
    
    
    
    
        
            
    
    

    
