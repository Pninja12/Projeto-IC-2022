#IMPORT LIBRARIES AND THE OTHER PYTHON FILES CONTAINING CLASSES AND FUNCTIONS
import time
import Clear_Screen
import Select_Units
from Unit_Classes import *

#DEFINE VARIABLES
Main_Loop = True

#FLAVOUR TEXT FOR WHEN THE GAME FIRST RUNS
print("Welcome to a Land of Aventure!")
print("We hope you enjoy the game!")

#MAIN LOOP CONTROLLED BY A VARIABLE SO THAT I CAN DECIDE TO REPLAY THE GAME OR EXIT OUT OF IT AT THE END
while Main_Loop == True:
    
    #STOPS THE CODE, ALLOWING TIME FOR THE USER TO READ THE FLAVOUR TEXT
    time.sleep(3)

    #CLEAN THE TERMINAL
    Clear_Screen.Clear_Screen()
    
    #RECEIVE THE INPUTS FOR HOW MANY UNITS THE PLAYER WANTS IN THE GAME AND CREATE THAT AMOUNT OF OBJECTS FROM THE CLASSES
    Warriors_List = Select_Units.Select_Units(Warrior(), "Warriors")
    Priests_Lists = Select_Units.Select_Units(Priest(), "Priests")
    OrcWarriors_List = Select_Units.Select_Units(Orc_Warrior(), "Orc Warriors")
    
    #CLEAN THE TERMINAL
    Clear_Screen.Clear_Screen()
    
    #FLAVOUR TEXT WHICH ALSO SERVES FOR THE PLAYER TO CONFIRM THAT HIS INPUTS HAVE BEEN TAKEN INTO ACCOUNT
    print("The party comprised of " + str(len(Warriors_List)) + " Warriors and " + str(len(Priests_Lists)) + " Priests arrived at a clearing when they were suddenly ambushed!")
    time.sleep(2)
    print("The party is surrounded by " + str(len(OrcWarriors_List)) + " Orc Warriors.")
    time.sleep(1)
    print("The battle is inevitable!")
    time.sleep(2)
    
    #CLEAN THE TERMINAL
    Clear_Screen.Clear_Screen()