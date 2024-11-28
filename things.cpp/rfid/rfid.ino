#include <SPI.h>
#include <MFRC522.h>
#include <Servo.h>

Servo servo;
 
#define SS_PIN 53
#define RST_PIN 5
#define CLOSED 90
#define OPEN 0
MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.
 
void setup() 
{
  pinMode(3, OUTPUT);
  Serial.begin(9600);   // Inicia a serial
  SPI.begin();      // Inicia  SPI bus
  mfrc522.PCD_Init();   // Inicia MFRC522
  servo.attach(7);
  servo.write(CLOSED);
}
 
void loop() 
{
  if (Serial.available() > 0) 
  {
    char inputChar = Serial.read();
    if (inputChar == '1') 
      servo.write(OPEN);
    else
      servo.write(CLOSED);
  }

  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }

  digitalWrite(3, HIGH);
  delay(100);
  digitalWrite(3, LOW);

  String newConteudo = "";
  
  //Mostra UID na serial
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     newConteudo.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     newConteudo.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  newConteudo.toUpperCase();
  
  Serial.println(newConteudo.substring(1));

  delay(2000);
}