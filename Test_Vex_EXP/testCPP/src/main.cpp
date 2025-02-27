/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       jarvisn                                                   */
/*    Created:      2/27/2025, 5:25:21 PM                                     */
/*    Description:  EXP project                                               */
/*                                                                            */
/*----------------------------------------------------------------------------*/
#include "vex.h"

using namespace vex;

// A global instance of vex::brain used for printing to the EXP brain screen
vex::brain       Brain;

// define your global instances of motors and other devices here


int main() {

    Brain.Screen.printAt( 2, 30, "Hello EXP" );

    // Create the Brain.
brain Brain;
// Construct an analog_in "analogIn" with the
// analog_in class.
analog_in analogIn = analog_in(Brain.ThreeWirePort.A);


    while(1) {
       
        // Allow other tasks to run
        this_thread::sleep_for(10);
    }

}





