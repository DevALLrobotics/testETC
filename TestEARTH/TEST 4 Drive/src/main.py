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
from MotorDrive import _Motor 

    
MotorDrive = _Motor(100,BRAKE)

MotorDrive.Forward()
wait(1,SECONDS)
MotorDrive.Stop()
wait(1,SECONDS)
MotorDrive.ForwardFWD()
wait(1,SECONDS)
MotorDrive.StopFWD()

