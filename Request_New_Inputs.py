#IMPORT
import Clear_Screen
import time

def Request_New_Inputs():
    #INFORM THE PLAYER THAT HIS INPUT IS INVALID
    print("Invalid input!")
    print("Please try again!")
    
    #PAUSE THE CODE TO MAKE SURE THE PLAYER HAS ENOUGH TIME TO READ
    time.sleep(2)

    #CLEAR THE SCREEN TO AVOID INFORMATION OVERLOAD
    Clear_Screen.Clear_Screen()