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

class _Motor():
    def __init__(self,M1,M2,M3,M4,Velocity,StopTypes):
        self.M1 = M1
        self.M2 = M2
        self.M3 = M3
        self.M4 = M4
        self.Velocity = Velocity
        self.StopTypes = StopTypes

    