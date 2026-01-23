#include <Keypad.h>

const byte ROWS = 4, COLS = 4;
const int ledpin = 13;

char keys[ROWS][COLS] = {
  {'1','2','3','C'},
  {'4','5','6','D'},
  {'7','8','9','B'},
  {'*','0','#','A'}

};

byte rowPins[ROWS] = {2,3,4,5};
byte colPins[COLS] = {6,7,8,9};

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup(){ 
  pinMode(ledpin, OUTPUT);
  digitalWrite(ledpin, HIGH);
  Serial.begin(9600); 

  }
void loop(){

  char k = keypad.getKey();
  if(k) Serial.println(k), tone(10, 1010, 30);
  
}
