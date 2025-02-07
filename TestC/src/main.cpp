#include "vex.h"
#include "led_control.h"

using namespace vex;

brain Brain;
led myLED(Brain.ThreeWirePort.A);  // เชื่อมต่อ LED กับพอร์ต A

int main() {
    LEDControl ledController(myLED);
    
    while (true) {
        ledController.turnOn();
        vex::task::sleep(1000); // เปิดไฟ 1 วินาที
        
        ledController.turnOff();
        vex::task::sleep(1000); // ปิดไฟ 1 วินาที
        
        ledController.blink(500); // กระพริบ 500 มิลลิวินาที
        
        vex::task::sleep(2000); // พัก 2 วินาทีก่อนเริ่มรอบใหม่
    }
}
