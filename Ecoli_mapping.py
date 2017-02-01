# -*- coding: utf-8 -*-
"""
Created: Mon Jun 27 17:34:10 2016
Author: matthewrobinson (Python 3.5)

Description:
"""
import numpy as np
import matplotlib.pyplot as plt

import csv

#list of things to be mapped to
with open('EVfold_7-26-16_IDs_for_mapping.csv', 'r') as f:
  reader = csv.reader(f)
  temp_IDs = list(reader)

# the 3 column entry you draw data from
with open('EVfold_newdata_9-5-2016.csv', 'r') as f:
  reader = csv.reader(f)
  temp_data = list(reader)
  
IDs = np.array(temp_IDs)
data = np.array(temp_data)

dt = np.dtype((str, 2000))   # 35-character string

mapping = np.empty((IDs.size,3),dt)

id_count = 0
for id in IDs:
    data_count = 0
    for name in data[:,0]:
        if id == name:
            mapping[id_count,0] = id[0]
            mapping[id_count,1] = data[data_count,1]
            mapping[id_count,2] = data[data_count,2]
        data_count = data_count + 1
    id_count = id_count + 1
    print(id_count)
