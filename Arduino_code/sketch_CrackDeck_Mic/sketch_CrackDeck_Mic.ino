#include <Keypad.h>

const byte ROWS = 4;
const byte COLS = 4;
const int ledpin = 13;

// Keypad setup
char keys[ROWS][COLS] = {
  {'1','2','3','C'},
  {'4','5','6','D'},
  {'7','8','9','B'},
  {'*','0','#','A'}
};
byte rowPins[ROWS] = {2,3,4,5};
byte colPins[COLS] = {6,7,8,9};
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

// Audio timing
unsigned long lastAudio = 0;
const int audioInterval = 1; // 1 ms ~1 kHz sample rate

void setup(){
  pinMode(ledpin, OUTPUT);
  digitalWrite(ledpin, HIGH);
  Serial.begin(115200); // fast enough for audio + buttons
}

void loop(){
  unsigned long now = millis();

  // 1️⃣ Send audio every ~1 ms
  if(now - lastAudio >= audioInterval){
    lastAudio = now;
    byte audioSample = analogRead(A0) >> 2; // convert 10-bit -> 8-bit
    Serial.write(0xAA);                     // audio tag
    Serial.write(audioSample);              // audio byte
  }

  // 2️⃣ Check keypad continuously
  char k = keypad.getKey();
  if(k){
    Serial.write(0xBB); // button tag
    Serial.write(k);    // button byte
    tone(10, 1010, 30); // short beep
  }
}