#ifndef LED_CONTROL_H
#define LED_CONTROL_H

#include "vex.h"

class LEDControl {
public:
    LEDControl(vex::digital_out &led);
    void turnOn();
    void turnOff();
    void blink(int duration);
    
private:
    vex::digital_out &ledPort;
};

#endif
