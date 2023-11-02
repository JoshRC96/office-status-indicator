//Defining each RGB pin with the board
int redPin = 11;
int bluePin = 10;
int greenPin = 9;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //Setting serial communication to communicate with the Python script
  pinMode(redPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(greenPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    String officeStatus = Serial.read(); //read variable value from Python script through the serial port and will be "busy", "not bussy", or "off"
    if (officeStatus == "busy") {
      digitalWrite(redPin, HIGH);
      digitalWrite(bluePin, LOW);
      digitalWrite(greenPin, LOW);
    } else if (officeStatus == "not busy") {
      digitalWrite(redPin, HIGH);
      digitalWrite(bluePin, HIGH);
      digitalWrite(greenPin, HIGH);
    } else {
      digitalWrite(redPin, LOW);
      digitalWrite(bluePin, LOW);
      digitalWrite(greenPin, LOW);
    }
  }
}
