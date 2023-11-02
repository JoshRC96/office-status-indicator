import serial #importing the serial module from the pyserial library to enable communication with the Arduino board.

ser = serial.Serial('COM3', 9600) #setting the serial communication

while True:
    officeStatus = input("Enter B for busy, N for not busy, and O for off (Enter any key to quit): ")
    if officeStatus == 'B' or officeStatus == 'N' or officeStatus == 'O':
        ser.write(officeStatus.encode()) #seding the signal to the Arduino board
    else:
        print("Good Bye")
        # turning off the LED before closing the Python program
        officeStatus = 'O'
        ser.write(officeStatus.encode())
        break