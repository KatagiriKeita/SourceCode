#!/usr/bin/env python3
#coding: utf-8
import csv
from math import *
import numpy as np

data = []
read_filename = 'Rehaimu3.5GHz_V_om_Pl_1_katagiri_data4.csv'
with open(read_filename,'r') as f:

    reader = csv.reader(f)
    next(reader)

    for row in csv.reader(f):

        a = row

        Rx_lat = float(a[3])
        Rx_lon = float(a[4])

        rssi_dBm = 10.0 * log10(float(a[6]))
        pl_dBm = rssi_dBm * (-1.0)
        pl_mW = pow(10,pl_dBm / 10.0)

        tmp = []
        tmp.append(Rx_lat)
        tmp.append(Rx_lon)
        tmp.append(pl_mW)
        data.append(tmp)

data = np.array(data)

data1 = []
read_filename = 'UEC2_rate200_20180625_220730_fieldtest_log.csv'
with open(read_filename,'r') as f:

    reader = csv.reader(f)

    for row in csv.reader(f):

        a = row

        measurement_date_unix = a[0]

        if (len(data1) < len(data)):

            data1.append(measurement_date_unix)

        else:

            break

data1 = np.array(data1)

data2 = np.c_[data1,data]

string = ['#measure_datetime','receive_lat','receive_lon','pl_value']
write_filename = 'test2.csv'
with open(write_filename,'w') as f:

    writer = csv.writer(f)
    writer.writerow(string)

    for row in data2:

        writer.writerow(row)
