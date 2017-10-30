#!usr/bin/python
#This code is written by Diresh Soomirte!

import MySQLdb
import serial

db = MySQLdb.connect("localhost","your_username","your_pw","your_db")
curs = db.cursor()
gps = serial.Serial("/dev/ttyACM0", baudrate =9600)
while True:
        line = gps.readline()
        data = line.split(",")
        if data[0] == "$GPRMC":
                if data[2] =="A":
                        raw_lat = data[3]
                        raw_long = data[5]
                        f_lat = float(raw_lat[:2])
                        s_lat = float(raw_lat[2:])
                        lat = round((( (s_lat/60)+f_lat )*(-1)),6)
                       # print round(lat,5)
                        f_long = float(raw_long[:3])
                        s_long = float(raw_long[3:])
                        long = round(( (s_long/60) + f_long),6)
                       # print round(long,5)
                        try:
                          curs.execute ("update data set latt=%s where id='0'" %lat)
                          curs.execute ("update data set longg=%s where id='0'" %long)
                          db.commit()
                          print "Data committed"
                        except:
                            print " Error: the database is being rolled back"
                            db.rollback()
