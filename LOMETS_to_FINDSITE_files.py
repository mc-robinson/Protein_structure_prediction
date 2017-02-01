# -*- coding: utf-8 -*-
"""
Created: Thu Jul 28 16:25:38 2016
Author: matthewrobinson (Python 3.5)

Description: Code to transfer LOMETS output into FINDSITE input
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import csv

#dir_name = "LOMETS_test_output"
#
import os
#dirList = os.listdir(dir_name)
#folders = np.array(dirList)

###usually use what's below but I have to deal with tar files
#mypath = "/Users/matthewrobinson/Documents/spyder/scratch/LOMETS_test_output/" #unnecessary I think
import glob
#newList = glob.glob('./LOMETS_dat_batch11/*/*.dat') #might have to change this
#fileArr = np.array(newList)

#for_tar_file stuff
newList = glob.glob('/Volumes/SysBio-1/SILVER\ LAB/Matt\ Robinson/LOMETS/LOMETSinitdatFiles/*')
fileArr = np.array(newList)

with open('FINDSITE_PDB_mapping.csv', 'r') as f:
  reader = csv.reader(f)
  temp_IDs = list(reader)
dt = np.dtype((str, 2000))  
FS_mapping = np.array(temp_IDs,dt)


#accession_name = "P22803" #this will have to be done uniquely for every file probably in the for loop
PDB_ids = dict({})

#count = 0
for file in fileArr:

    file_name = re.split("./LOMETS_dat_batch11/",file)[1]
    file_name = re.split("/init.dat",file_name)[0]
    print(file_name)
    
    temp_list = []
    
    temp_df = pd.read_table(file)
    dt = np.dtype((str, 2000))
    temp_arr = np.array(temp_df.values,dt)
    
    for i in range(0,temp_arr.size-1):
        if ("ATOM" not in temp_arr[i,0]) and ("TER" not in temp_arr[i,0]):
            str_list = re.split(' +',temp_arr[i,0])
            temp_list.append((str_list[len(str_list)-2]).upper()) #get the capitalized PDB file name
            
    unique_list = list(set(temp_list)) #gets rid of duplicates
    #PDB_ids[accession_name] = unique_list
    
    FS_PDB_list = []
    for PDB in unique_list:
        for j in range(0,FS_mapping.size-1):
            if (PDB in FS_mapping[j,0]):
                new_PDB = re.split(' +',FS_mapping[j,0])[1]
                FS_PDB_list.append(new_PDB)
    
    unique_FS_PDB = list(set(FS_PDB_list)) #gets rid of duplicates
    PDB_ids[file_name] = unique_FS_PDB
  
output_path = "/Users/matthewrobinson/Documents/spyder/scratch/files_for_FINDSITE/" 
for key in PDB_ids:
    file_string = output_path + key + ".templates.lst"
    f_output = open(str(file_string), 'w')
    
    for item in PDB_ids[key]:
        f_output.write("%s\n" % item)
    f_output.close()
    
    
        
            
    
    

    
