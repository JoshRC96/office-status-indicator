## office-status-indicator
This project will create a desktop app using Python to control an LED that will be used to indicate when an office is in use (RED = in use, WHITE = available)

The project is currently made up of two separate scripts. userApp.py is the Python script used to produce the desktop app containing the 
user interface used to set the office status. This script uses Tkinter to create the app window and all the features. Further, this script
is responsible for communicating with the Arduino sketch, using serial port communication, to change the color of the LED.

The second script is an Arduino sketch (ledControl.ino). This sketch is responsible for communicating with the Arduino UNO R3 board,
changing the color of the LED based on the signal received from userApp.py.

# Future Plans:
Improve the user interface and overall capability by adding a "custom color function", enabling the user to turn the RGB LED into 
other colors other than RED or WHITE.
