#IMPORT RANDOM SO THAT WE MAY SIMULATE THE DICE ROLLS
import random

#DEFINE FUNCTION WHICH RETURNS A LIST OF THE OBJECTS IN THE ORDER IN WHICH THEY ACT THIS TURN
def Turn_Order(List_Warrior, List_Priest, List_OrcWarrior):
    
    #PLACE ALL OBJECTS IN ONE SINGULAR LIST
    Unit_List = List_Warrior + List_Priest + List_OrcWarrior
    
    #CREATE EMPTY DICTIONARY IN ORDER TO SORT THE OBJECTS BY THEIR TURN ORDER
    Initiative_Order = {
    }
    
    #CALCULATE THE TURN ORDER FOR EVERY OBJECT AND PAIR IT WITH THE OBJECT ITSELF IN THE DICTIONARY
    for i in Unit_List:
        Initiative_Order[i.Init + random.randint(1,20)] = i
    
    #CREATE EMPTY LIST TO SAVE THE OBJECTS IN THE CORRECT ORDER 
    Ordered_Units = []
    
    #ITERATE THE DICTIONARY'S KEYS (TURN ORDER) ORDERED IN DECRESCENT ORDER
    for i in sorted(Initiative_Order.keys(), reverse = True):
        #APPEND THEIR CORRESPONDING VALUE (OBJECT) IN THE ARRAY
        Ordered_Units.append(Initiative_Order.get(i))
    
    #RETURN A LIST OF THE OBJECTS IN THE CORRECT ORDER
    return(Ordered_Units)