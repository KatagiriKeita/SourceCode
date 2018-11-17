#!/usr/bin/env python3
#coding: utf-8
import csv
from math import *
from datetime import datetime as dt
from datetime import timedelta

data = []
n = 0
packet_id = 0
read_filename = 'map_testdata_venus.csv'
with open(read_filename,'r') as f:

    reader = csv.reader(f)

    for row in csv.reader(f):

        a = row

        measure_date = a[0]
        Tx_lat = float(a[1])
        Tx_lon = float(a[2])
        Rx_lat = float(a[3])
        Rx_lon = float(a[4])
        frequency = float(a[6])
        pl_value = pow(10,int(a[7]) / 10.0)
        transmitter_id = int(a[11]) 

        tmp = []
        tmp.append(measure_date)
        tmp.append(Tx_lat)
        tmp.append(Tx_lon)
        tmp.append(Rx_lat)
        tmp.append(Rx_lon)
        tmp.append(frequency)
        tmp.append(pl_value)
        tmp.append(transmitter_id)
        tmp.append(packet_id)
        data.append(tmp)

        packet_id = packet_id + 1

string = ['#measure_datetime','trans_lat','trans_lon','receive_lat','receive_lon','frequency','rssi','transmitter_id','packet_id']
write_filename = 'map_testdata_venus_convert.csv'
with open(write_filename,'w') as f:

    writer = csv.writer(f)
    writer.writerow(string)

    for row in data:

        writer.writerow(row)

#data2 = []
#n = 0
#for row in data:
#
#    a = row
#    n = n + 1
#
#    measure_date = a[0]
#    measure_date_time = dt.strptime(measure_date,'%Y/%m/%d %H:%M:%S.%f')
#    measure_date_time1 = measure_date_time + timedelta(days = n)
#    measure_date_time1 = measure_date_time1.strftime('%Y/%m/%d %H:%M:%S.%f')
#    print(measure_date_time1)
#    Tx_lat = float(a[1])
#    Tx_lon = float(a[2])
#    Rx_lat = float(a[3]) + 0.00001
#    Rx_lon = float(a[4]) + 0.00001
#    frequency = float(a[5])
#    pl_value = float(a[6])
#    transmitter_id = int(a[7]) + 1
#
#    tmp = []
#    tmp.append(measure_date_time1)
#    tmp.append(Tx_lat)
#    tmp.append(Tx_lon)
#    tmp.append(Rx_lat)
#    tmp.append(Rx_lon)
#    tmp.append(frequency)
#    tmp.append(pl_value)
#    tmp.append(transmitter_id)
#    data2.append(tmp)
#
#write_filename = 'map_testdata_venus_convert2.csv'
#with open(write_filename,'w') as f:
#
#    writer = csv.writer(f)
#
#    for row in data2:
#
#        writer.writerow(row)
#
#data3 = []
#n = 0
#for row in data2:
#
#    a = row
#    n = n + 1
#
#    measure_date = a[0]
#    measure_date_time = dt.strptime(measure_date,'%Y/%m/%d %H:%M:%S.%f')
#    measure_date_time1 = measure_date_time + timedelta(days = n)
#    measure_date_time1 = measure_date_time1.strftime('%Y/%m/%d %H:%M:%S.%f')
#    print(measure_date_time1)
#    Tx_lat = float(a[1])
#    Tx_lon = float(a[2])
#    Rx_lat = float(a[3]) + 0.00000001
#    Rx_lon = float(a[4]) + 0.00000001
#    frequency = float(a[5])
#    pl_value = float(a[6])
#    transmitter_id = int(a[7]) + 1
#
#    tmp = []
#    tmp.append(measure_date_time1)
#    tmp.append(Tx_lat)
#    tmp.append(Tx_lon)
#    tmp.append(Rx_lat)
#    tmp.append(Rx_lon)
#    tmp.append(frequency)
#    tmp.append(pl_value)
#    tmp.append(transmitter_id)
#    data3.append(tmp)
#
#write_filename = 'map_testdata_venus_convert3.csv'
#with open(write_filename,'w') as f:
#
#    writer = csv.writer(f)
#
#    for row in data3:
#
#        writer.writerow(row)
