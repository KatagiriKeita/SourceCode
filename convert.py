#!/usr/bin/env python3
#coding: utf-8
import csv
from datetime import datetime

frequency = 760e6 #rewrite
Tx_lat = 35.697893 #rewrite
Tx_lon = 139.751289 #rewrite
Tx_id = 'A0001' #rewrite

flag_jst = 1 #rewrite

data = []
read_filename = 'test1.csv'
with open(read_filename,'r') as f:

    reader = csv.reader(f)

    for row in csv.reader(f):

        a = row

        s = a[0]
        if (s.find('#') != -1):

            continue

        else:

            measure_datetime_unix = float(a[0])

            if (flag_jst):

                measure_datetime_jst = datetime.fromtimestamp(measure_datetime_unix)
                measure_datetime_jst = measure_datetime_jst.strftime('%Y/%m/%d %H:%M:%S.%f')
                tmp = []
                tmp.append(measure_datetime_jst)

            else:

                measure_datetime_utc = datetime.utcfromtimestamp(measure_datetime_unix)
                measure_datetime_utc = measure_datetime_utc.strftime('%Y/%m/%d %H:%M:%S.%f')
                tmp = []
                tmp.append(measure_datetime_utc)

            Rx_lat = float(a[1])
            Rx_lon = float(a[2])
            pl_value = float(a[3])

            tmp.append(Tx_lat)
            tmp.append(Tx_lon)
            tmp.append(Rx_lat)
            tmp.append(Rx_lon)
            tmp.append(frequency)
            tmp.append(pl_value)
            tmp.append(Tx_id)

            data.append(tmp) 


string = ['#measure_datetime','trans_lat','trans_lon','receive_lat','receive_lon','frequency','rssi','transmitter_id'] #do not rewrite 
write_filename = 'test_pl.csv'
with open(write_filename,'w') as f:

    writer = csv.writer(f)
    writer.writerow(string)

    for row in data:

        writer.writerow(row)




