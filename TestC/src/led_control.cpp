#include "vex.h"
#include "led_control.h"

LEDControl::LEDControl(vex::led &led) : ledPort(led) {}

void LEDControl::turnOn() {
    ledPort.on();
}

void LEDControl::turnOff() {
    ledPort.off();
}

void LEDControl::blink(int duration) {
    ledPort.on();
    vex::task::sleep(duration);
    ledPort.off();
    vex::task::sleep(duration);
}
