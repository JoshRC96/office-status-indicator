//Defining each RGB pin with the board
int redPin = 11;
int greenPin = 10;
int bluePin = 9;

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
    char officeStatus = Serial.read(); //read variable value from Python script through the serial port and will be 'B', 'N', or 'O'
    if (officeStatus == 'B') {
      digitalWrite(redPin, HIGH);
      digitalWrite(greenPin, LOW);
      digitalWrite(bluePin, LOW);
    } else if (officeStatus == 'N') {
      digitalWrite(redPin, HIGH);
      digitalWrite(greenPin, HIGH);
      digitalWrite(bluePin, HIGH);
    } else {
      digitalWrite(redPin, LOW);
      digitalWrite(greenPin, LOW);
      digitalWrite(bluePin, LOW);
    }
  }
}
