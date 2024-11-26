#include <Ultrasonic.h>

Ultrasonic ultrasonic(4, 5);
Ultrasonic ultrasonic2(6, 7);
int distance;
int distance2;
int distance3;

void setup() {
  Serial.begin(9600);
}

void loop() {
  distance = ultrasonic.read();
  distance2 = ultrasonic2.read();
  distance3 = ultrasonic3.read();
  
  Serial.println("{\"vaga1\": " + (String) distance + ", \"vaga2\": " + (String) distance2 + ", \"vaga3\": " + (String) distance2 + "}");

  delay(500);
}
