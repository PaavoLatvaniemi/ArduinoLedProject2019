const int ledPin = 9;
int brightness = 0;
int fadeAmount = 50;


void setup() {
    pinMode(ledPin, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    if(Serial.available()){
        char serialListener = Serial.read();
        if(serialListener == 'H'){
             brightness = brightness + fadeAmount;
             if (brightness > 255) {
                brightness = 255;
             }
        }
        
        if(serialListener == 'L'){
            brightness = brightness + -fadeAmount; 
            if (brightness < 0) {
                brightness = 0;
            }
        }  
        analogWrite(ledPin, brightness);
        Serial.println(brightness);
        Serial.flush();
    }
}
