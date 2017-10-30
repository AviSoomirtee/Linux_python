#This code is written by Diresh Soomirtee!

import serial

gps = serial.Serial("/dev/ttyACM0", baudrate = 9600)

while True:
        line = gps.readline()
        data = line.split(",")
        if data[0] == "$GPRMC":
                if data[2] =="A":
                        raw_lat = data[3]
                        raw_long = data[5]
                        f_lat = float(raw_lat[:2])
                        s_lat = float(raw_lat[2:])
                        lat = (( (s_lat/60)+f_lat )*(-1))
                        print round(lat,5)
                        f_long = float(raw_long[:3])
                        s_long = float(raw_long[3:])
                        long = ( (s_long/60) + f_long)
                        print round(long,5)
                #       print f_long
                #       print "Laltitude: %s" % (data[3])
                #       print "longitude: %s" % (data[5]) 
