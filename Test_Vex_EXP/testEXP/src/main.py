# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       jarvisn                                                      #
# 	Created:      2/27/2025, 3:01:27 PM                                        #
# 	Description:  EXP project                                                  #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Create the Brain.
brain = Brain()
# digital_in_a = DigitalIn(brain.three_wire_port.a)
motor_4 = Motor(Ports.PORT4, True)
# x = AnalogIn(brain.three_wire_port.a)


# Construct a PotentiometerV2 "pot2" with the PotentiometerV2 class.
pot2 = PotentiometerV2(brain.three_wire_port.a)


print("start")
while True:
    # test = digital_in_a.value()
    # test = analog_in.value()
    test = pot2.value()
    # print(f"test: {test}")
    print(test)
    # print(type(test))
    # if test == 1:
    #     motor_4.spin(FORWARD,50,PERCENT)
    # else:
    #     motor_4.stop()
    
    wait(100,MSEC)
    
