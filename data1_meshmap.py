#!/usr/bin/env python3
#coding: utf-8
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import csv

data = pd.read_csv("data.csv")
#data = pd.read_csv("data_interpolated_10m.csv")
#data = pd.read_csv("data_interpolated_shadowing_classifier.csv")
#data = pd.read_csv("data_interpolated_pathloss.csv")

#print(data)
df_data_pivot = pd.pivot_table(data = data,values = 'r',columns ='x',index ='y')
#print(df_data_pivot)

#sorted_x = df_data_pivot.sortlevel(["x","y"],ascending=[False,False],sort_remaining=False)

x_list = []
with open('data.csv','r') as f:

    reader = csv.reader(f)

    next(reader)

    for row in csv.reader(f):

        a = row

        x_list.append(int(a[0]))


y_list = [4341] * len(x_list)
#print(dir(sns))

#sns.heatmap(df_data_pivot,cmap = "RdYlGn_r",robust = True,linewidths = .5,linecolor = "black",square = True)
#sns.heatmap(df_data_pivot,vmax = -30,vmin = -85,cmap = "RdYlGn_r",robust = True,square = True)
#sns.heatmap(df_data_pivot,vmax = -30,vmin = -85,cmap = "RdYlGn_r",robust = True,square = True,xticklabels = False,yticklabels = False)
#sns.heatmap(df_data_pivot,vmax = -40,vmin = -130,cmap = "RdYlGn_r",robust = True,square = True)
sns.heatmap(df_data_pivot,vmax = -40,vmin = -140,cmap = "jet",robust = True,square = True)
#sns.heatmap(df_data_pivot,vmax = -40,vmin = -140,cmap = "gnuplot",robust = True,square = True)
#sns.heatmap(df_data_pivot,vmax = -40,vmin = -100,cmap = "jet",robust = True,square = True)
#sns.heatmap(df_data_pivot,cmap = "RdYlGn_r",robust = True,square = True)
#sns.heatmap(df_data_pivot,cmap = "RdYlGn_r",linecolor = "black",square = True)
#sns.heatmap(df_data_pivot,cmap = "Reds",linewidths = .5,linecolor = "black",square = True)
#plt.gca().invert_yaxis()
plt.plot([6012,6012],[4341,4352],color = 'black')
plt.show()
