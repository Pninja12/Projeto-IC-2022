#IMPORTS
import time

#BASIC FUNCTION TO PROVIDE A BIT OF GRAPHICAL FEEDBACK AS WELL AS WAIT FOR THE PLAYER'S INPUT TO PROCEED
def Wait_Input():
    print("")
    print(".")
    time.sleep(0.3)
    print("..")
    time.sleep(0.3)
    print("...")
    time.sleep(0.3)
    input("Press ENTER when you're ready to proceed. ")