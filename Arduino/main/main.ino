#include <Wire.h>

#define MOTOR_PIN 2
#define PUMP_PIN 3

byte RxByte;
bool valueMotor;
bool valuePump;

void I2C_RxHandler(int numBytes)
{
  while(Wire.available()) {  // Read Any Received Data
    valueMotor = false;
    valuePump = false;
    RxByte = Wire.read();

    if (RxByte == 0x01) {
      valueMotor = true;
    } else if (RxByte == 0x10) {
      valuePump = true;
    } else if (RxByte == 0x11) {
      valueMotor = true;
      valuePump = true;
    }
  }
}

void setup() {
  pinMode(MOTOR_PIN, OUTPUT);
  Wire.begin(0x2f);
  Wire.onReceive(I2C_RxHandler);
}

void loop() {
  digitalWrite(MOTOR_PIN, valueMotor);
  digitalWrite(PUMP_PIN, valuePump)
  delay(100);
}
