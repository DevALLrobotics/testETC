const int pin = 23;  // ใช้ขาที่รองรับ digital output

void setup() {
    pinMode(pin, OUTPUT);
}

void loop() {
    // ไม่ต้องทำอะไร เพราะเราตั้งให้ HIGH ตั้งแต่ setup
    digitalWrite(pin, HIGH);  // ตั้งขาให้เป็น HIGH
    delay(3000);
    digitalWrite(pin, LOW);  // ตั้งขาให้เป็น HIGH
    delay(3000);

}
