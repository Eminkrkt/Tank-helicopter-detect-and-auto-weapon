import serial
import time
ser = serial.Serial('/dev/ttyUSB0',timeout=1)  # open serial port
time.sleep(2)
print(ser.name)         # check which port was really used

ser.write(bytes("75.25,148.24" , 'utf-8'))
ser.close()  