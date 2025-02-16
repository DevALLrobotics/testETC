# Library imports
from vex import *
# from MotorDrive import _Motor


brain = Brain()

motor_main_left = Motor(Ports.PORT7, 1.0, False)
motor_spin_left = Motor(Ports.PORT9, 1.0, False)
motor_spin_right = Motor(Ports.PORT10, 1.0, True)
motor_main_right = Motor(Ports.PORT12, 1.0, True)

Pneumatic5 = Pneumatic(Ports.PORT5)

Pneumatic5.pump_on()

class Pneumatic_Control:
    def __init__(self):
        pass

    def TWD(self):
        Pneumatic5.extend(CYLINDER1)
    def FWD(self):
        Pneumatic5.retract(CYLINDER1)




 

class Drive_Control:
    class TWD():
        def __init__(self):
            self.brain_inertial = Inertial()
            self.Pneumatics = Pneumatic_Control()
            self.left_drive_smart = MotorGroup(motor_main_left, motor_spin_left)
            self.right_drive_smart = MotorGroup(motor_main_right, motor_spin_right)
            self.drivetrain_TWD = SmartDrive(motor_main_left, motor_main_right, self.brain_inertial, 200)     


        def Forward(self,Distance,Velocity):
            self.Pneumatics.TWD()
            self.drivetrain_TWD.drive_for(FORWARD, Distance, MM, Velocity, PERCENT, wait=True)

        def Reverse(self,Distance,Velocity):
            self.Pneumatics.TWD()
            self.drivetrain_TWD.drive_for(REVERSE, Distance, MM, Velocity, PERCENT, wait=True)
        
        def Left(self,Degree,Velocity):
            self.Pneumatics.TWD()
            self.drivetrain_TWD.turn_for(LEFT, Degree, DEGREES, Velocity, PERCENT, wait=True)

        def Right(self,Degree,Velocity):
            self.Pneumatics.TWD()
            self.drivetrain_TWD.turn_for(RIGHT, Degree, DEGREES, Velocity, PERCENT, wait=True)
        
        def Stop_TWD(self):
            motor_main_left.stop()
            motor_main_right.stop()


    class FWD():
        def __init__(self):
            self.brain_inertial = Inertial()
            self.Pneumatics = Pneumatic_Control()
            self.left_drive_smart = MotorGroup(motor_main_left, motor_spin_left)
            self.right_drive_smart = MotorGroup(motor_main_right, motor_spin_right)
            self.drivetrain_FWD = SmartDrive(self.left_drive_smart, self.right_drive_smart, self.brain_inertial, 200)


        def Forward(self,Distance,Velocity):
            self.Pneumatics.FWD()
            self.drivetrain_FWD.drive_for(FORWARD, Distance,MM, Velocity, PERCENT, wait=True)
        
        def Reverse(self,Distance,Velocity):
            self.Pneumatics.TWD()
            self.drivetrain_FWD.drive_for(REVERSE, Distance, MM, Velocity, PERCENT, wait=True)
        
        def Left(self,Degree,Velocity):
            self.Pneumatics.TWD()
            self.drivetrain_FWD.turn_for(LEFT, Degree, DEGREES, Velocity, PERCENT, wait=True)

        def Right(self,Degree,Velocity):
            self.Pneumatics.TWD()
            self.drivetrain_FWD.turn_for(RIGHT, Degree, DEGREES, Velocity, PERCENT, wait=True)

        def Stop_FWD(self):
            motor_main_left.stop()
            motor_main_right.stop()
            motor_main_left.stop()
            motor_main_right.stop()
        

Drive = Drive_Control()
Pneumatics = Pneumatic_Control()


Drive.TWD.Forward(Distance = 300, Velocity = 50)
Drive.FWD.
Drive.Stop_FWD()

Pneumatics.TWD()




