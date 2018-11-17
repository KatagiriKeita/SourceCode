#!/usr/bin/env python3
#coding: utf-8
import csv
from datetime import datetime

data = []
date = []
cnt_list = []
list_date = []
sec_before = 0.0
cnt = 0
flag = 1



#read_filename = 'UEC2_20180608_202023_fieldtest_log.csv'
read_filename = 'UEC2_rate400_20180625_220257_fieldtest_log.csv'
with open(read_filename,'r') as f:
    reader = csv.reader(f)

    for row in csv.reader(f):

        tmp = []
        a = row

        if (flag):

            #unixtime = float(a[1])
            unixtime = float(a[0])
            transmission_date_before = datetime.fromtimestamp(unixtime)
            print(unixtime)
            flag = 0

        modulation_type = int(a[17])
        mac_add = a[18]
        packet_length = int(a[6])
        packet = a[8]
        #a[1] = float(a[1])
        a[0] = float(a[0])
        #transmission_date3 = datetime.fromtimestamp(a[1])
        transmission_date3 = datetime.fromtimestamp(a[0])
        transmission_date3 = transmission_date3.strftime('%Y/%m/%d %H:%M:%S.%f')
        tmp.append(transmission_date3)
        tmp.append(packet)
        list_date.append(tmp)

        #1秒間の送信パケット数カウント(Macアドレスで抽出)
        if (mac_add == '04:e5:48:20:14:6c'):
            #print(packet)

            date1 = []
            cnt_list1 = []
            a[0] = float(a[0])
            #a[1] = float(a[1])
            #transmission_date = datetime.fromtimestamp(a[1])
            transmission_date = datetime.fromtimestamp(a[0])
            d = transmission_date - transmission_date_before
            d_sec = d.seconds
            #print(d_sec)
            

            #sec = transmission_date.second
            #sec_diff = sec - sec_before
            #print(sec_diff)
            if (d_sec >= 1.0):
                #print('packet_num = %s,cnt = %d' % (packet,cnt))
                #print(transmission_date,transmission_date_before,d_sec,packet)
                #print(cnt)
                transmission_date1 = transmission_date.strftime('%Y/%m/%d %H:%M:%S.%f')
                cnt_list1.append(transmission_date1)
                cnt_list1.append(packet)
                cnt_list1.append(cnt)
                cnt_list.append(cnt_list1)
                cnt = 0
                transmission_date_before = transmission_date

            else:
                cnt = cnt + 1

            transmission_date = transmission_date.strftime('%Y/%m/%d %H:%M:%S.%f')
            date1.append(transmission_date)
            date1.append(packet)
            date.append(date1)



        #マップ化に必要なデータ抽出(変調方式とパケット長で抽出) 
        #if ((modulation_type == 11) and (packet_length == 356)):
        if (mac_add == '04:e5:48:20:14:6c'):
            data2 = []

            a[0] = float(a[0])
            measurement_date = datetime.fromtimestamp(a[0])
            measurement_date = measurement_date.strftime('%Y/%m/%d %H:%M:%S.%f')

            Tx_lat = a[2]
            Tx_lon = float(a[3]) + 180.0
            Rx_lat = a[9]
            Rx_lon = float(a[10]) + 180.0

            freq = 5890e6
            rssi_dBm = a[13]

            data2.append(measurement_date)
            data2.append(Tx_lat)
            data2.append(Tx_lon)
            data2.append(Rx_lat)
            data2.append(Rx_lon)
            data2.append(freq)
            data2.append(rssi_dBm)
            data.append(data2)


string = ['#measure_datetime','trans_lat','trans_lon','receive_lat','receive_lon','frequency','rssi']
#write_filename = 'UEC2_20180608_202023_fieldtest_log_extra10.csv'
#write_filename = 'UEC2_20180608_202023_fieldtest_log_extra11.csv'
#write_filename = 'UEC2_20180608_202023_fieldtest_log_extra.csv'
write_filename = 'UEC2_rate200_20180625_220730_fieldtest_log_extra.csv'
with open(write_filename,'w') as f:
    writer = csv.writer(f)

    writer.writerow(string)

    for row in data:

        writer.writerow(row)



#data = []
#read_filename = 'UEC2_20180608_202023_fieldtest_log.csv'
#with open(read_filename,'r') as f:
#    reader = csv.reader(f)
#
#    for row in csv.reader(f):
#
#        a = row
#
#        mac_add = a[18]
#        if (mac_add == '04:e5:48:20:14:6c'):
#
#            data.append(a)
#
#
#write_filename = 'UEC2_20180608_202023_fieldtest_log_extra_mac.csv'
#with open(write_filename,'w') as f:
#    writer = csv.writer(f)
#
#    for row in data:
#
#        writer.writerow(row)




#write_filename = 'transmission_date.csv'
#with open(write_filename,'w') as f:
#    writer = csv.writer(f)
#
#    for row in date:
#
#        writer.writerow(row)


write_filename = 'transmission_rate.csv'
with open(write_filename,'w') as f:
    writer = csv.writer(f)

    for row in cnt_list:

        writer.writerow(row)


write_filename = 'transmission_date.csv'
with open(write_filename,'w') as f:
    writer = csv.writer(f)

    for row in list_date:

        writer.writerow(row)
