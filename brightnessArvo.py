#!/usr/bin/python
# -*- coding: UTF-8 -*-
import serial
import json

ser = serial.Serial('/dev/ttyACM0',9600)
while True:
    data = ser.readline().decode("utf-8").rstrip('\r\n')
    json_data = json.dumps([{'valo': data}])
    with open('/var/www/html/valo.json', 'w') as outfile:
        json.dump(json.JSONDecoder().decode(json_data), outfile)
    
    print (json_data)
ser.close()