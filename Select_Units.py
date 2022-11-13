#IMPORTS
from Unit_Classes import *

#DEFINE FUNCTION WHICH RETURNS A LIST OF OBJECTS OF THE DESIRED CLASS
def Select_Units(ClassName):
    
    #CREATE EMPTY LIST TO STORE THE OBJECTS
    Units_List = []
    
    #INITIATE NUMBER SO WE CAN REPRESENT THE DIFFERENT OBJECTS OF THE SAME TYPE
    Number = 0

    #IF THE DESIRED CLASS IS THE ORC_WARRIOR
    if ClassName == "Orc Warrior_":
        #ITERATE IN A RANGE FROM 0 TO X (NUMBER CHOSEN BY THE PLAYER)
        for i in range(0,int(input("How many Orc Warriors will appear? "))):
            #APPEND X OBJECTS OF THE ORC_WARRIOR CLASS TO THE LIST
            Units_List.append(Orc_Warrior())

    #IF THE DESIRED CLASS IS THE WARRIOR
    elif ClassName == "Warrior_":
        #ITERATE IN A RANGE FROM 0 TO X (NUMBER CHOSEN BY THE PLAYER)
        for i in range(0,int(input("How many Warriors are in the party? "))):
            #APPEND X OBJECTS OF THE WARRIOR CLASS TO THE LIST
            Units_List.append(Warrior())

    #IF THE DESIRED CLASS IS THE PRIEST
    else:
        #ITERATE IN A RANGE FROM 0 TO X (NUMBER CHOSEN BY THE PLAYER)
        for i in range(0,int(input("How many Priests are in the party? "))):
            #APPEND X OBJECTS OF THE PRIEST CLASS TO THE LIST
            Units_List.append(Priest())

    print("")
    
    #RETURN THE LIST OF OBJECTS OF THE DESIRED CLASS    
    return Units_List