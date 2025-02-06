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
# from MotorDrive import _Motor


brain = Brain()

motor_7 = Motor(Ports.PORT7, 1.0, True)
motor_8 = Motor(Ports.PORT8, 1.0, True)
motor_9 = Motor(Ports.PORT9, 1.0, True)
motor_10 = Motor(Ports.PORT10, 1.0, True)

class Motor_Control:
    class Forward:
        def __init__(self,Velocity):
            self.M1 = motor_7
            self.M2 = motor_8
            self.M3 = motor_9
            self.M4 = motor_10
            self.Velocity = Velocity
        def TWD(self):
            self.M1.spin(FORWARD,self.Velocity)
            self.M2.spin(FORWARD,self.Velocity)
        def FWD(self):
            self.M1.spin(FORWARD,self.Velocity)
            self.M2.spin(FORWARD,self.Velocity)
            self.M3.spin(FORWARD,self.Velocity)
            self.M4.spin(FORWARD,self.Velocity)

    class Stop:
        def __init__(self,StopTypes):
            self.M1 = motor_7
            self.M2 = motor_8
            self.M3 = motor_9
            self.M4 = motor_10
            self.StopTypes = StopTypes
        def TWD(self):
            self.M1.stop()
            self.M2.stop()
        def FWD(self):
            self.M1.stop()
            self.M2.stop()
            self.M3.stop()
            self.M4.stop()
    



        

   



MotorForward = Motor_Control.Forward(100)
MotorStop = Motor_Control.Stop(BRAKE)
MotorForward.TWD()
wait(1,SECONDS)
MotorStop.TWD()

