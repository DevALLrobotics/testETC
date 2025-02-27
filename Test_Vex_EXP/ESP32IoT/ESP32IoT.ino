#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "ชื่อ WiFi";  // เปลี่ยนเป็น WiFi ของคุณ
const char* password = "รหัสผ่าน WiFi";
const char* serverUrl = "http://192.168.1.100:5000/get_pin";  // เปลี่ยนเป็น IP ของคอมพิวเตอร์ที่รัน Flask API
const int pin = 23;  // ใช้ขาที่รองรับ digital output

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to WiFi");
}

void loop() {
    if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;
        http.begin(serverUrl);

        int httpResponseCode = http.GET();
        if (httpResponseCode > 0) {
            String response = http.getString();
            Serial.println("Response from Server: " + response);

            // วิเคราะห์ JSON
            int pin = response.substring(response.indexOf("\"pin\":") + 6, response.indexOf(", \"state\"")).toInt();
            String state = response.substring(response.indexOf("\"state\":") + 9, response.lastIndexOf("\""));

            pinMode(pin, OUTPUT);
            if (state == "HIGH") {
                digitalWrite(pin, HIGH);
            } else {
                digitalWrite(pin, LOW);
            }
        } else {
            Serial.println("Error getting data");
        }
        http.end();
    }
    delay(5000);  // อัปเดตค่าทุกๆ 5 วินาที
}
