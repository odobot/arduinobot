#include <Servo.h>

Servo motor;

void setup(){
  motor.attach(8);
  motor.write(90);

  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop(){
  if(Serial.available())
  {
    int angle = Serial.readString().toInt();
    motor.write(angle);
  }

  delay(0.1);
}
