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

motor_7 = Motor(Ports.PORT7, 1.0, False)
motor_9 = Motor(Ports.PORT9, 1.0, False)
motor_10 = Motor(Ports.PORT10, 1.0, True)
motor_12 = Motor(Ports.PORT12, 1.0, True)
Pneumatic5 = Pneumatic(Ports.PORT5)

motor_main_left = motor_7
motor_spin_left = motor_9
motor_spin_right = motor_10
motor_main_right = motor_12

Pneumatic5.pump_on()



        
class Motor_Control:
    class TWD:
        class Forward_For:
            def __init__(self,Stering,Velocity,Degree):
                self.M1 = motor_main_left
                self.M4 = motor_main_right
                self.Stering = Stering
                self.Velocity = Velocity
                self.Degree = Degree
                self.Pneumatic = Pneumatic5
                self.Pneumatic.extend(CYLINDER1)
                self.M1.set_position(0,DEGREES)
                self.M4.set_position(0,DEGREES)
                if Stering>=0:
                    while self.M1.position(DEGREES) < self.Degree :
                        self.M1.spin(FORWARD,self.Velocity)
                        self.M4.spin(FORWARD,(self.Velocity-self.Stering))
                else:
                    while self.M4.position(DEGREES) < self.Degree :
                        self.M1.spin(FORWARD,(self.Velocity+self.Stering))
                        self.M4.spin(FORWARD,self.Velocity)

        class stop:
            def __init__(self,StopTypes):
                self.M1 = motor_main_left
                self.M4 = motor_main_right
                self.StopTypes = StopTypes

                self.Pneumatic = Pneumatic5
                self.Pneumatic.extend(CYLINDER1)

                self.M1.set_stopping(self.StopTypes)
                self.M4.set_stopping(self.StopTypes)
                self.M1.stop()
                self.M4.stop()
            


    class FWD:
        class Forward_For:
            def __init__(self,Stering,Velocity,Degree):
                self.M1 = motor_main_left
                self.M2 = motor_spin_left
                self.M3 = motor_spin_right
                self.M4 = motor_main_right
                self.Stering = Stering
                self.Velocity = Velocity
                self.Degree = Degree
                self.Pneumatic = Pneumatic5
                self.Pneumatic.retract(CYLINDER1)
                self.M1.set_position(0,DEGREES)
                self.M4.set_position(0,DEGREES)
                if Stering>=0:
                    while self.M1.position(DEGREES) < self.Degree :
                        self.M1.spin(FORWARD,self.Velocity)
                        self.M2.spin(FORWARD,self.Velocity)
                        self.M3.spin(FORWARD,(self.Velocity-self.Stering))
                        self.M4.spin(FORWARD,(self.Velocity-self.Stering))
                else:
                    while self.M4.position(DEGREES) < self.Degree :
                        self.M1.spin(FORWARD,(self.Velocity+self.Stering))
                        self.M2.spin(FORWARD,(self.Velocity+self.Stering))
                        self.M3.spin(FORWARD,self.Velocity)
                        self.M4.spin(FORWARD,self.Velocity)

        class stop:
            def __init__(self,StopTypes):
                self.M1 = motor_main_left
                self.M2 = motor_spin_left
                self.M3 = motor_spin_right
                self.M4 = motor_main_right
                self.StopTypes = StopTypes

                self.Pneumatic = Pneumatic5
                self.Pneumatic.retract(CYLINDER1)

                self.M1.set_stopping(self.StopTypes)
                self.M2.set_stopping(self.StopTypes)
                self.M3.set_stopping(self.StopTypes)
                self.M4.set_stopping(self.StopTypes)
                self.M1.stop()
                self.M2.stop()
                self.M3.stop()
                self.M4.stop()



