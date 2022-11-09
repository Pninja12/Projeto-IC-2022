#DEFINE FUNCTION WHICH RETURNS A LIST OF OBJECTS OF THE DESIRED CLASS
def Select_Units(Class, Name):
    
    #CREATE EMPTY LIST TO STORE THE OBJECTS
    Units_List = []
    
    #ITERATE IN A RANGE FROM 0 TO X (NUMBER CHOSEN BY THE PLAYER)
    if Name == "Orc Warriors":
        for i in range(0,int(input("How many " + Name + " will appear? "))):
            #APPEND X OBJECTS OF THE DESIRED CLASS TO THE LIST
            Units_List.append(Class)
    else:
        for i in range(0,int(input("How many " + Name + " are in the party? "))):
            #APPEND X OBJECTS OF THE DESIRED CLASS TO THE LIST
            Units_List.append(Class)
            
    print("")
    
    #RETURN THE LIST OF OBJECTS OF THE DESIRED CLASS    
    return Units_List