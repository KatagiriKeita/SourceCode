#!/usr/bin/env python3
#coding: utf-8
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from math import *

data = []
pl_list = []
print('Please input the csv file : ',end = "")
read_filename = input()
with open(read_filename,'r') as f:

    reader = csv.reader(f)

    for row in csv.reader(f):

        a = row

        s = a[0]
        if (s.find('#') != -1):

            continue

        else:
        
            Rx_mesh = a[3]
            Rx_mesh = Rx_mesh.split('-')

            Rx_x = Rx_mesh[1][1] + Rx_mesh[2][1] + Rx_mesh[3][1] + Rx_mesh[4][1] + Rx_mesh[5][1]
            Rx_y = Rx_mesh[1][0] + Rx_mesh[2][0] + Rx_mesh[3][0] + Rx_mesh[4][0] + Rx_mesh[5][2]
            #Rx_y = (-1) * int(Rx_y)

            pl_dBm = 10.0 * log10(float(a[13]))
            
            tmp = []
            tmp.append(Rx_x)
            tmp.append(Rx_y)
            tmp.append(pl_dBm)
            data.append(tmp)

            pl_list.append(pl_dBm)

pl_min = min(pl_list)
pl_max = max(pl_list)


string = ['x','y','v']
write_filename = 'data.csv'
with open(write_filename,'w') as f:

    writer = csv.writer(f)
    writer.writerow(string)

    for row in data:

        writer.writerow(row)

map_data = pd.read_csv('data.csv')
df_data_pivot = pd.pivot_table(data = map_data,values = 'v',columns = 'x',index = 'y')

#sns.heatmap(df_data_pivot,vmax = pl_max,vmin = pl_min,cmap = 'jet',robust = True,square = True, xticklabels = False, yticklabels = False)
sns.heatmap(df_data_pivot,vmax = pl_max,vmin = pl_min,cmap = 'jet',robust = True,square = True, xticklabels = True, yticklabels = True)

plt.show()
