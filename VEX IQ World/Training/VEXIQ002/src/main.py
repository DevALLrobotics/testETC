# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       EARTH                                                        #
# 	Created:      2/9/2025, 10:57:24 AM                                        #
# 	Description:  IQ2 project                                                  #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain = Brain()
controller = Controller()


Stat_robot = 0

class Display:
    def __init__(self,Size,Color,Row,Colum):
        self.Size = Size
        self.Color = Color
        self.Row = Row
        self.Colum = Colum
    def print(self,Text):
        self.Text = Text
        brain.screen.set_font(self.Size)
        brain.screen.set_pen_color(self.Color)
        brain.screen.set_cursor(self.Row,self.Colum)
        brain.screen.print(self.Text)



def ClearDisplay():
    wait(0.2,SECONDS)
    brain.screen.clear_screen()


def Set_Stat_robot():
    global Stat_robot
    if Stat_robot == 0:
        Stat_robot = 1
    else:
        Stat_robot = 0


def Stat_robot_Control():
    while True:
        if controller.buttonRUp.pressing():
            Set_Stat_robot()
            while controller.buttonRUp.pressing():
                pass

def Stat_Print():
    while True:
        MotorLeft = controller.axisA.position() + controller.axisC.position()
        MotorRight = controller.axisA.position() - controller.axisC.position()
        if Stat_robot == 0:
            Mode.print("Mode 2")
            Main.print("Main L="+str(MotorLeft)+" Main R="+str(MotorRight))
            ClearDisplay()
        else:
            Mode.print("Mode 4")
            Main.print("Main L="+str(MotorLeft)+" Main R="+str(MotorRight))
            Spin.print("Spin L="+str(MotorLeft)+" Spin R="+str(MotorRight))
            ClearDisplay()


Mode = Display(FontType.MONO30,Color.BLUE,1,3)
Main = Display(FontType.MONO12,Color.RED,4,1)
Spin = Display(FontType.MONO12,Color.GREEN,5,1)



event_Stat_robot_Control = Event()
event_Stat_Print = Event()

event_Stat_robot_Control(Stat_robot_Control)
event_Stat_Print(Stat_Print)

event_Stat_robot_Control.broadcast()
event_Stat_Print.broadcast()
