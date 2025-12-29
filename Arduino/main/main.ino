#include <Wire.h>

#define MOTOR_PIN 2
#define PUMP_PIN 3

byte RxByte;
bool valueMotor = false;
bool valuePump = false;

void I2C_RxHandler(int numBytes)
{
  while(Wire.available()) {  // Read Any Received Data
    RxByte = Wire.read();

    valueMotor = RxByte & 0x01;
    valuePump = RxByte & 0x02;
    
    // Debugging
    // Serial.println("Motor "); Serial.println(valueMotor);
    // Serial.println("Pump "); Serial.println(valuePump);
  }
}

void setup() {
  Serial.begin(9600);
  pinMode(MOTOR_PIN, OUTPUT);
  pinMode(PUMP_PIN, OUTPUT);
  Wire.begin(0x2f);
  Wire.onReceive(I2C_RxHandler);
}

void loop() {
  digitalWrite(MOTOR_PIN, valueMotor);
  digitalWrite(PUMP_PIN, valuePump);
  delay(100);
}
