//Coded By Ahmet YILDIRIM
//www.mclightning.com
//mclightning34@hotmail.com
//Code license:GNU General Public License v3

#include <IRremote.h>

int RECV_PIN = 8;
int led=11;
IRrecv irrecv(RECV_PIN);

decode_results results;
void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn(); // Start the receiver
  pinMode(led,OUTPUT);
}
void bip() {
 digitalWrite(led,HIGH);
 delay(100);
 digitalWrite(led,LOW); 
}
void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(results.value);
    bip();
    irrecv.resume(); // Receive the next value
  }
}

