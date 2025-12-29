#define MOTOR_PIN 2
#define PUMP_PIN 3

bool valueMotor = false;
bool valuePump = false;

void setup() {
  Serial.begin(9600);

  pinMode(MOTOR_PIN, OUTPUT);
  pinMode(PUMP_PIN, OUTPUT);
}

void loop() { 
  digitalWrite(MOTOR_PIN, valueMotor);
  digitalWrite(PUMP_PIN, valuePump);
  delay(100);
}
