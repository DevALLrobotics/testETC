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
    def __init__(self,Velocity,StopTypes):
        self.M1 = motor_7
        self.M2 = motor_8
        self.M3 = motor_9
        self.M4 = motor_10
        self.Velocity = Velocity
        self.StopTypes = StopTypes

    def Forward(self):
        self.M1.spin(FORWARD,self.Velocity)
        self.M2.spin(FORWARD,self.Velocity)
    
    def Stop(self):
        self.M1.stop(self.StopTypes)
        self.M2.stop(self.StopTypes)

    def ForwardFWD(self):
        self.M1.spin(FORWARD,self.Velocity)
        self.M2.spin(FORWARD,self.Velocity)
        self.M3.spin(FORWARD,self.Velocity)
        self.M4.spin(FORWARD,self.Velocity)
    
    def StopFWD(self):
        self.M1.stop(self.StopTypes)
        self.M2.stop(self.StopTypes)
        self.M3.stop(self.StopTypes)
        self.M4.stop(self.StopTypes)