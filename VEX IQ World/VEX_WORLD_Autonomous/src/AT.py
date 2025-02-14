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

class Pneumatic_Control:
    def __init__(self):
        pass
    def TWD(self):
        Pneumatic5.extend(CYLINDER1)
    def FWD(self):
        Pneumatic5.retract(CYLINDER1)




 

class Drive_Control:
    def __init__(self):
        pass

    def Forward_TWD(self,Degree,Velocity):
        P = Pneumatic_Control()
        P.TWD()
        brain_inertial = Inertial()
        drivetrain = SmartDrive(motor_main_left, motor_main_right, brain_inertial, 200)
        drivetrain.drive_for(FORWARD, Degree, MM, Velocity, PERCENT, wait=True)



    def REVERSE_FWD(self,Degree,Velocity):
        P = Pneumatic_Control()
        P.FWD()
        brain_inertial = Inertial()
        left_drive_smart = MotorGroup(motor_main_left, motor_spin_left)
        right_drive_smart = MotorGroup(motor_main_right, motor_spin_right)
        drivetrain = SmartDrive(left_drive_smart, right_drive_smart, brain_inertial, 200)
        drivetrain.drive_for(REVERSE, Degree, MM, Velocity, PERCENT, wait=True)



    def Stop_TWD(self):
        motor_main_left.stop()
        motor_main_right.stop()
    
    def Stop_FWD(self):
        motor_main_left.stop()
        motor_main_right.stop()
        motor_main_left.stop()
        motor_main_right.stop()
        

D = Drive_Control()


D.Forward_TWD(300,50)
D.REVERSE_FWD(300,50)
D.Forward_TWD(1,50)

D.Stop_FWD()


