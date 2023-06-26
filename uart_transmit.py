# Python code transmits a byte to Arduino /Microcontroller


import serial
import time

#COMPort_Name = input("Enter COM Port number -")

SerialObj = serial.Serial('/dev/ttyACM0')

								   # COMxx   format on Windows
                                   #/dev/ttyUSBx format on Linux
                                   #
                                   #Eg /dev/ttyUSB0
                                   #SerialObj = serial.Serial('/dev/ttyUSB0')
                                   #SerialObj = serial.Serial('COM11',9600)

print(SerialObj) #display default parameters

time.sleep(3)   # Only needed for Arduino,For AVR/PIC/MSP430 & other Micros not needed
                # opening the serial port from Python will reset the Arduino.
                # Both Arduino and Python code are sharing Com11 here.
                # 3 second delay allows the Arduino to settle down.

SerialObj.baudrate = 9600  # set Baud rate to 9600
SerialObj.bytesize = 8     # Number of data bits = 8
SerialObj.parity   ='N'    # No parity
SerialObj.stopbits = 1     # Number of Stop bits = 1

print(SerialObj)

BytesWritten = SerialObj.write(b'100')

#Convert String to Byte format

num = 255
num1 = 10
# integer to bytes
num_bytes = num.to_bytes(1, byteorder='little')
num_bytes1 = num1.to_bytes(1, byteorder='big')
SerialObj.write(num_bytes)
#SerialObj.write(num_bytes1)
print(num_bytes)

#SerialObj.close()
