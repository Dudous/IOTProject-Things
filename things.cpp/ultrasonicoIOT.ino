#include <Ultrasonic.h>
#include <Servo.h>

Servo servo;

Ultrasonic ultrasonic(4, 5);
Ultrasonic ultrasonic2(6, 7);
int distance;
int distance2;


void setup() {
  Serial.begin(9600);
  pinMode(11, OUTPUT);
}

void loop() {
  distance = ultrasonic.read();
  distance2 = ultrasonic.read();
  Serial.println("{\"vaga1\": " + (String) distance + ", \"vaga2\": " + (String) distance2 + "}");
  if(distance < 50)
  {
    for(int i=0; i<90; i++)
    digitalWrite(11, HIGH);
  }
  else
  {
    digitalWrite(11, LOW);
  }
  delay(500);
}