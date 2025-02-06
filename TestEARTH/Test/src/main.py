# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       EARTH                                                        #
# 	Created:      2/6/2025, 11:51:10 AM                                        #
# 	Description:  IQ2 project                                                  #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

motor_7 = Motor(Ports.PORT7, 1.0, True)
motor_8 = Motor(Ports.PORT8, 1.0, True)
motor_9 = Motor(Ports.PORT9, 1.0, True)
motor_10 = Motor(Ports.PORT10, 1.0, True)

touch_12 = Touchled(Ports.PORT12)

touch_12.set_brightness(100)
touch_12.set_color(Color.BLUE)