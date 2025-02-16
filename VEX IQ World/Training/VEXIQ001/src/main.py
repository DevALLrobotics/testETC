
from vex import *

brain = Brain()

Motor1 = Motor(Ports.PORT1,1.0,False)
Motor2 = Motor(Ports.PORT2,1.0,True)
Motor3 = Motor(Ports.PORT3,1.0,False)
Motor4 = Motor(Ports.PORT4,1.0,True)

class Motor_Control:
    class Mode_2_Motor:
        def __init__(self,Velocity):
            self.Velocity = Velocity
        def Forward(self):
            Motor1.spin(FORWARD,self.Velocity)
            Motor2.spin(FORWARD,self.Velocity)
        def Reverse(self):
            Motor1.spin(REVERSE,self.Velocity)
            Motor2.spin(REVERSE,self.Velocity)
        def Left(self):
            Motor1.spin(REVERSE,self.Velocity)
            Motor2.spin(FORWARD,self.Velocity)
        def Right(self):
            Motor1.spin(FORWARD,self.Velocity)
            Motor2.spin(REVERSE,self.Velocity)
        def stop(self):
            Motor1.stop()
            Motor2.stop()

    class Mode_4_Motor:
        def __init__(self,Velocity):
            self.Velocity = Velocity
        def Forward(self):
            Motor1.spin(FORWARD,self.Velocity)
            Motor2.spin(FORWARD,self.Velocity)
            Motor3.spin(FORWARD,self.Velocity)
            Motor4.spin(FORWARD,self.Velocity)
        def Reverse(self):
            Motor1.spin(REVERSE,self.Velocity)
            Motor2.spin(REVERSE,self.Velocity)
            Motor3.spin(REVERSE,self.Velocity)
            Motor4.spin(REVERSE,self.Velocity)
        def Left(self):
            Motor1.spin(REVERSE,self.Velocity)
            Motor2.spin(FORWARD,self.Velocity)
            Motor3.spin(REVERSE,self.Velocity)
            Motor4.spin(FORWARD,self.Velocity)
        def Right(self):
            Motor1.spin(FORWARD,self.Velocity)
            Motor2.spin(REVERSE,self.Velocity)
            Motor3.spin(FORWARD,self.Velocity)
            Motor4.spin(REVERSE,self.Velocity)
        def stop(self):
            Motor1.stop()
            Motor2.stop()
            Motor3.stop()
            Motor4.stop()



TWD = Motor_Control.Mode_2_Motor(100)
FWD = Motor_Control.Mode_4_Motor(100)


TWD.Forward()
wait(2,SECONDS)

TWD.Reverse()
wait(2,SECONDS)

FWD.Left()
wait(2,SECONDS)

FWD.Right()
wait(2,SECONDS)