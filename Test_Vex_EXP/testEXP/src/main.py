# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       jarvisn                                                      #
# 	Created:      2/27/2025, 3:01:27 PM                                        #
# 	Description:  EXP project                                                  #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Create the Brain.
brain = Brain()
digital_in_a = DigitalIn(brain.three_wire_port.a)

# test for see value input A 

print("start")
while True:
    test = digital_in_a.value()
    print(test)
    wait(1,SECONDS)
    
