bool pinIsHigh[] = {false, false, false, false, false, false, false, false, false, false, false, false, false, false};

void setup() {
  Serial.begin(9600);
  pinMode(2,INPUT_PULLUP);
  pinMode(3,INPUT_PULLUP);
  pinMode(4,INPUT_PULLUP);
  pinMode(5,INPUT_PULLUP);
  pinMode(6,INPUT_PULLUP);
  pinMode(7,INPUT_PULLUP);
  pinMode(8,INPUT_PULLUP);
  pinMode(9,INPUT_PULLUP);
  pinMode(10,INPUT_PULLUP);
  pinMode(11,INPUT_PULLUP);
  pinMode(12,INPUT_PULLUP);
  pinMode(13,INPUT_PULLUP);
  pinMode(14,INPUT_PULLUP);
  pinMode(15,INPUT_PULLUP);
  pinMode(16,INPUT_PULLUP);
}

void loop() {
  for (int pin = 2; pin <= 15; pin++) {
    if ((digitalRead(pin) == HIGH) && (pinIsHigh[pin-2] == false)) {
      pinIsHigh[pin-2] = true;
      if (digitalRead(16) == HIGH) {
        Serial.println(255-pin, DEC);
      }
      else {
        Serial.println(pin, DEC);
      }
      delay(1000);
      pinIsHigh[pin-2] = false;
    }
  }
}
