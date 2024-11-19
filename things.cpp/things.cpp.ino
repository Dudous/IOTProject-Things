#include <Arduino.h>


//==== Inclusão de bibliotecas ====//
#include <VirtualWire.h>


void setup()
{
    vw_set_tx_pin(5);
    Serial.begin(9600);    // Debugging only
    Serial.println("setup");

    // Initialise the IO and ISR
    vw_set_ptt_inverted(true); // Required for DR3100
    vw_setup(500);   // Bits per sec

    pinMode(13, OUTPUT);
}

void loop()
{
    byte x[1];

    x[0] = 0;

    digitalWrite(13, HIGH);
    
    for(int i = 0;i <= 255; i+=5){
        x[0] = i;
        vw_send(x, 1);
        vw_wait_tx();
        Serial.println(i);
    }

    digitalWrite(13, LOW);

    for(int i = 255;i >= 0; i-=5){
        x[0] = i;
        vw_send(x, 1);
        vw_wait_tx();
    }

}//endLoop
