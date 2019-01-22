#!/usr/bin/python
# -*- coding: UTF-8 -*-
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
mystring = "H"
b = mystring.encode('utf-8')

ser.write(b)
ser.close()
print("""Content-type:text/html\n\n""")