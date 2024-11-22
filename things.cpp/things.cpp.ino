#include <SPI.h>
#include <MFRC522.h>
 
#define SS_PIN 53
#define RST_PIN 5
MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.
 
void setup() 
{
  Serial.begin(9600);   // Inicia a serial
  SPI.begin();      // Inicia  SPI bus
  mfrc522.PCD_Init();   // Inicia MFRC522
}
 
void loop() 
{
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
