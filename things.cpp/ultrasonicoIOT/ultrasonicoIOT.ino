#include <Ultrasonic.h>

Ultrasonic ultrasonic(4, 5);
Ultrasonic ultrasonic2(6, 7);
Ultrasonic ultrasonic3(8, 9);
int distance;
int distance2;
int distance3;

void setup() {
  Serial.begin(9600);
}

void loop() {
  distance = ultrasonic.read();
  delay(30);
  distance2 = ultrasonic2.read();
  delay(30);
  distance3 = ultrasonic3.read();
  
  Serial.println("{\"vaga1\": " + (String) distance + ", \"vaga2\": " + (String) distance2 + ", \"vaga3\": " + (String) distance3 + "}");

  delay(1000);
}
