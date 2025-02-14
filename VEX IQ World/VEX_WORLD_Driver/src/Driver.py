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

motor_main_left = Motor(Ports.PORT7, 1.0, False)
motor_spin_left = Motor(Ports.PORT9, 1.0, False)
motor_spin_right = Motor(Ports.PORT10, 1.0, True)
motor_main_right = Motor(Ports.PORT12, 1.0, True)

motor_shooter_left = Motor(Ports.PORT3, 1.0, False)
motor_shooter_right = Motor(Ports.PORT4, 1.0, True)

Bumper11 = Bumper(Ports.PORT11)

Pneumatic5 = Pneumatic(Ports.PORT5)
Pneumatic2 = Pneumatic(Ports.PORT2)
Pneumatic1 = Pneumatic(Ports.PORT1)
Pneumatic6 = Pneumatic(Ports.PORT6)

controller = Controller()



def PneumaticTWD():
    Pneumatic5.extend(CYLINDER1)
def PneumaticFWD():
    Pneumatic5.retract(CYLINDER1)

def PneumaticShooter():
    Pneumatic2.extend(CYLINDER2)
    Pneumatic5.extend(CYLINDER2)
def PneumaticShooterToSpin():
    Pneumatic2.retract(CYLINDER2)
    Pneumatic5.retract(CYLINDER2)

def PneumaticSpinTopUp():
    Pneumatic1.retract(CYLINDER1)
    Pneumatic6.retract(CYLINDER1)
def PneumaticSpinTopDown():
    Pneumatic1.extend(CYLINDER1)
    Pneumatic6.extend(CYLINDER1)

def PneumaticIntakUp():
    Pneumatic2.retract(CYLINDER1)
    Pneumatic6.retract(CYLINDER2)
def PneumaticIntakDown():
    Pneumatic2.extend(CYLINDER1)
    Pneumatic6.extend(CYLINDER2)
       
class Motor_Control:
    class TWD:
        class Drive:
            def __init__(self,Stering,Velocity):
                V_Left = Velocity+Stering
                V_Right = Velocity-Stering
                PneumaticTWD()
                motor_main_left.spin(FORWARD,V_Left)
                motor_main_right.spin(FORWARD,V_Right)

        class Stop:
            def __init__(self,StopTypes):
                motor_main_left.set_stopping(StopTypes)
                motor_main_right.set_stopping(StopTypes)
                PneumaticTWD()
                motor_main_left.stop()
                motor_main_right.stop()

    class FWD:
        class Drive:
            def __init__(self,Stering,Velocity):
                V_Left = Velocity+Stering
                V_Right = Velocity-Stering
                PneumaticFWD()
                motor_main_left.spin(FORWARD,V_Left,PERCENT)
                motor_spin_left.spin(FORWARD,V_Left,PERCENT)
                motor_main_right.spin(FORWARD,V_Right,PERCENT)
                motor_spin_right.spin(FORWARD,V_Right,PERCENT)

        class Stop:
            def __init__(self,StopTypes):
                motor_main_left.set_stopping(StopTypes)
                motor_spin_left.set_stopping(StopTypes)
                motor_main_right.set_stopping(StopTypes)
                motor_spin_right.set_stopping(StopTypes)
                PneumaticFWD()
                motor_main_left.stop()
                motor_spin_left.stop()
                motor_main_right.stop()
                motor_spin_right.stop()


class Intak_Control:
    class Spin:
         def In():
             motor_spin_left.spin(REVERSE,100,PERCENT)
             motor_spin_right.spin(REVERSE,100,PERCENT)
         def Out():
             motor_spin_left.spin(FORWARD,100,PERCENT)
             motor_spin_right.spin(FORWARD,100,PERCENT)
         def Stop():
             motor_spin_left.stop()
             motor_spin_right.stop()


class Shooter_Control:
    def ShootUp():
        PneumaticSpinTopUp()
        PneumaticShooter()
        motor_shooter_left.spin(FORWARD,100,PERCENT)
        motor_shooter_right.spin(FORWARD,100,PERCENT)
    def ShootDown():
        PneumaticSpinTopDown()
    def ToSpinIn():
        motor_shooter_left.spin(REVERSE,100,PERCENT)
        motor_shooter_right.spin(REVERSE,100,PERCENT)
    def ToSpinOut():
        motor_shooter_left.spin(FORWARD,100,PERCENT)
        motor_shooter_right.spin(FORWARD,100,PERCENT)
    def Stop():
        motor_shooter_left.stop()
        motor_shooter_right.stop()






Stat_Data_DriveTrain = 0
Stat_Data_Intak = 0
Stat_Data_IntakUpDown = 0
Stat_Data_Shooter = 0





        


def Stat_Intak():
    global Stat_Data_Intak
    while True:
        if controller.buttonLUp.pressing():
            Stat_Data_Intak = 1
        elif controller.buttonLDown.pressing():
            Stat_Data_Intak = 2
        elif controller.buttonEUp.pressing():
            Stat_Data_Intak = 0

def Robot_Intak():
    global Stat_Data_DriveTrain
    global Stat_Data_Intak
    while True:
        if Stat_Data_DriveTrain == 0:
            if Stat_Data_Intak == 0:
                Intak_Control.Spin.Stop()
                if Stat_Data_Shooter != 1:
                    PneumaticShooterToSpin()
                    Shooter_Control.Stop()

            elif Stat_Data_Intak == 1:
                Intak_Control.Spin.In()
                if Stat_Data_Shooter != 1:
                    PneumaticShooterToSpin()
                    Shooter_Control.ToSpinIn()

            elif Stat_Data_Intak == 2:
                Intak_Control.Spin.Out()
                if Stat_Data_Shooter != 1:
                    PneumaticShooterToSpin()
                    Shooter_Control.ToSpinOut()


def Stat_IntakUpDown():
    global Stat_Data_IntakUpDown
    while True:
        if controller.buttonRDown.pressing():
            if Stat_Data_IntakUpDown == 0:
                Stat_Data_IntakUpDown = 1
            else:
                Stat_Data_IntakUpDown = 0
            while controller.buttonRDown.pressing():
                pass

def Robot_IntakUpDown():
    global Stat_Data_IntakUpDown
    while True:
        if Stat_Data_IntakUpDown == 0:
            if Bumper11.pressing():
                PneumaticIntakDown()
                wait(0.5,SECONDS)
            else:
                PneumaticIntakUp()
        else:
            PneumaticIntakDown()



def Stat_Shooter():
    global Stat_Data_Shooter
    global Stat_Data_DriveTrain
    global Stat_Data_Intak
    while True:
        if controller.buttonFUp.pressing():
            Stat_Data_Shooter = 1
        elif controller.buttonFDown.pressing():
            Stat_Data_Shooter = 2
            Stat_Data_DriveTrain = 0
            Stat_Data_Intak = 1
        else:
            Stat_Data_Shooter = 0

def Robot_Shooter():
    global Stat_Data_Shooter
    while True:
        if Stat_Data_Shooter == 1:
            Shooter_Control.ShootUp()
        elif Stat_Data_Shooter == 2:
            Shooter_Control.ShootDown()






def Stat_DriveTrain():
    global Stat_Data_DriveTrain
    while True:
        if controller.buttonRUp.pressing():
            if Stat_Data_DriveTrain == 0:
                Stat_Data_DriveTrain = 1
            else:
                Stat_Data_DriveTrain = 0
            while controller.buttonRUp.pressing():
                pass

def Robot_DriveTrain():
    Analog = 10
    while True:
        A = controller.axisA.position()
        C = controller.axisC.position()
        if Stat_Data_DriveTrain == 0:
            if A > Analog or A < -Analog or C > Analog or C < -Analog:
                Motor_Control.TWD.Drive(C,A)
            else:
                Motor_Control.TWD.Stop(BRAKE)
        else:
            if A > Analog or A < -Analog or C > Analog or C < -Analog:
                Motor_Control.FWD.Drive(C,A)
            else:
                Motor_Control.FWD.Stop(BRAKE)





event_Stat_DriveTrain = Event()
event_Robot_DriveTrain = Event()
event_Stat_DriveTrain(Stat_DriveTrain)
event_Robot_DriveTrain(Robot_DriveTrain)


event_Stat_Intak = Event()
event_Robot_Intak = Event()
event_Stat_Intak(Stat_Intak)
event_Robot_Intak(Robot_Intak)


event_Stat_Shooter = Event()
event_Robot_Shooter = Event()
event_Stat_Shooter(Stat_Shooter)
event_Robot_Shooter(Robot_Shooter)



event_Stat_IntakUpDown = Event()
event_Robot_IntakUpDown = Event()
event_Stat_IntakUpDown(Stat_IntakUpDown)
event_Robot_IntakUpDown(Robot_IntakUpDown)

event_Stat_DriveTrain.broadcast()
event_Robot_DriveTrain.broadcast()
event_Stat_Intak.broadcast()
event_Robot_Intak.broadcast()
event_Stat_Shooter.broadcast()
event_Robot_Shooter.broadcast()
event_Stat_IntakUpDown.broadcast()
event_Robot_IntakUpDown.broadcast()