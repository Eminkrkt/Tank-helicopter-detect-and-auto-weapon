"""
liste = [(246.), (130.), (626.), (417.)]

intx = liste[0] + (liste[2] - liste[0])
inty = liste[1] + (liste[3] - liste[1])
print(int(intx))
print(int(inty))
"""

"""
import cv2

im0 = cv2.imread("ALTAY.jpg")
while True:
    img = cv2.imshow("d",im0)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
"""
    
"""
liste = [0.85, "Tank" ,177, 45, 0.89, "Helikopter", 255, 102]
for a in range(0,len(liste)):
    if((a % 2 == 0 and a == 0) or a % 4 == 0):
        print("tam bolundu " + str(liste[a]))
    else :
        print("tam bolunmedi " + str(liste[a]))
"""


import serial
ser = serial.Serial('/dev/ttyUSB0',timeout=2)  # open serial port
print(ser.name)         # check which port was really used

ser.write(bytes("98.25,112.24" , 'utf-8'))
data = ser.read()
print(data)
ser.close()  