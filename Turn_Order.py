#IMPORT RANDOM SO THAT WE MAY SIMULATE THE DICE ROLLS
import time
import random
from collections import defaultdict

#DEFINE FUNCTION WHICH RETURNS A LIST OF THE OBJECTS IN THE ORDER IN WHICH THEY ACT THIS TURN
def Turn_Order(List_Priest, List_Warrior, List_OrcWarrior):
    
    #PLACE ALL OBJECTS IN ONE SINGULAR LIST
    Unit_List = List_Priest + List_Warrior + List_OrcWarrior
    
    #CREATE EMPTY DICTIONARY IN ORDER TO SORT THE OBJECTS BY THEIR TURN ORDER
    Initiative_Order = defaultdict(list)
    
    #CALCULATE THE TURN ORDER FOR EVERY OBJECT AND PAIR IT WITH THE OBJECT ITSELF IN THE DICTIONARY
    for i in Unit_List:

        #RANDOMIZE THE DICE ROLL
        Dice_Roll = random.randint(1,20)

        #APPEND THE INITIATIVE VALUE + DICE ROLE (TURN ORDER) AS THE KEY AND THE LIST OF CORRESPONDING OBJECTS TO THE DICTIONARY
        Initiative_Order[i.Init + Dice_Roll].append(i)
        time.sleep(0.3)
        if i in List_Priest:
            print(str(i.Name) + str(List_Priest.index(i)) + " has a base initiative of " + str(i.Init) +
            ". The dice landed on " + str(Dice_Roll) + ". The total initiative is " + str(i.Init+Dice_Roll) + ".")

        elif i in List_Warrior:
            print(str(i.Name) + str(List_Warrior.index(i)) + " has a base initiative of " + str(i.Init) + 
            ". The dice landed on " + str(Dice_Roll) + ". The total initiative is " + str(i.Init+Dice_Roll) + ".")

        else:
            print(str(i.Name) + str(List_OrcWarrior.index(i)) + " has a base initiative of " + str(i.Init) +
            ". The dice landed on " + str(Dice_Roll) + ". The total initiative is " + str(i.Init+Dice_Roll) + ".")


    #CREATE EMPTY LISTS TO SAVE THE LISTS OF OBJECTS IN THE CORRECT ORDER 
    Ordered_Units = []
    Ordered_Units2 = []
    
    #ITERATE THE DICTIONARY'S KEYS (TURN ORDER) ORDERED IN DECRESCENT ORDER
    for i in sorted(Initiative_Order, reverse = True):
        #APPEND THEIR CORRESPONDING VALUE (LIST OF OBJECTS) INTO ANOTHER LIST
        Ordered_Units.append(Initiative_Order.get(i))

    #NEED TO SEPERATE THE OBJECTS WHICH HAVE THE SAME TURN ORDER
    #ITERATE THROUGH THE LIST
    for i in Ordered_Units:
        #ITERATE THROUGH THE LIST OF OBJECTS
        for x in i:
            #APPEND EACH OBJECT IN THE PROPER ORDER TO THE CORRECT LIST
            Ordered_Units2.append(x)
    
    #RETURN A LIST OF THE OBJECTS IN THE CORRECT ORDER
    return(Ordered_Units2)