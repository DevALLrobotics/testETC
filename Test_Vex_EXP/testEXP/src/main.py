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
digital_in_a = DigitalIn(brain.three_wire_port.a)
motor_4 = Motor(Ports.PORT4, True)


print("start")
while True:
    test = digital_in_a.value()
    print(test)
    # print(type(test))
    if test == 1:
        motor_4.spin(FORWARD,50,PERCENT)
    else:
        motor_4.stop()
    wait(100,MSEC)
    
