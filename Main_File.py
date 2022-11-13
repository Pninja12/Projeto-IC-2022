#IMPORT LIBRARIES AND THE OTHER PYTHON FILES CONTAINING CLASSES AND FUNCTIONS
import time
import Clear_Screen
import Select_Units
import Turn_Order
import Wait_Input
import Print_Stats
import Request_New_Inputs
from Unit_Classes import *

#DEFINE VARIABLES
Main_Loop = True
Turn = 0

#FLAVOUR TEXT FOR WHEN THE GAME FIRST RUNS
print("Welcome to a Land of Aventure!")
print("We hope you enjoy the game!")

#STOPS THE CODE, ALLOWING TIME FOR THE USER TO READ THE FLAVOUR TEXT
time.sleep(3)

#MAIN LOOP CONTROLLED BY A VARIABLE SO THAT I CAN DECIDE TO REPLAY THE GAME OR EXIT OUT OF IT AT THE END
while Main_Loop == True:

    #CLEAN THE TERMINAL
    Clear_Screen.Clear_Screen()
    
    #RECEIVE THE INPUTS FOR HOW MANY UNITS THE PLAYER WANTS IN THE GAME AND CREATE THAT AMOUNT OF OBJECTS FROM THE CLASSES
    Warriors_List = Select_Units.Select_Units(Warrior().Name)
    Priests_List = Select_Units.Select_Units(Priest().Name)
    OrcWarriors_List = Select_Units.Select_Units(Orc_Warrior().Name)

    #CREATE THE ALLY LIST WHICH IS COMPRISED OF THE OBJECTS IN THE WARRIOR LIST AND THE PRIESTS LIST
    Ally_List = Warriors_List + Priests_List

    #CLEAN THE TERMINAL
    Clear_Screen.Clear_Screen()
    
    #FLAVOUR TEXT WHICH ALSO SERVES FOR THE PLAYER TO CONFIRM THAT HIS INPUTS HAVE BEEN TAKEN INTO ACCOUNT
    print("The party comprised of " + str(len(Warriors_List)) + " Warriors and " + str(len(Priests_List)) + " Priests arrived at a clearing when they were suddenly ambushed!")
    time.sleep(1)
    print("The party is surrounded by " + str(len(OrcWarriors_List)) + " Orc Warriors.")
    time.sleep(1)

    #IF EITHER OF THE SIDES HAVE NO UNITS
    if Ally_List == [] or OrcWarriors_List == []:
                
                #IMMEDIATELY END THE GAME
                Game_Loop = False
                print("Due to the lack of units, the battle is over before it even began!")
                time.sleep(3)
                
                #ASK IF THE PLAYER WANTS TO REMATCH
                Choice = True
                while Choice == True:
                    Clear_Screen.Clear_Screen()
                    print("Would you like a rematch? (y/n)")
                    Rematch = input("> ")
                    
                    #IF YES, RESTART THE GAME FROM THE MAIN LOOP
                    if Rematch.lower() == "y":
                        Choice = False
                        print("The battle shall restart.")
                        time.sleep(1)
                        print("Hope you have fun!")
                        pass

                    #IF NOT, BREAK ALL LOOPS AND QUIT FROM THE PROGRAM
                    elif Rematch.lower() == "n":
                        Choice = False
                        Main_Loop = False
                        print("Thank you for playing!")
                        time.sleep(1)
                        print("Hope you had a good time!")

                    #IF THERE'S NOT A VALID OPTION, ALLOW THE PLAYER TO RETRY THEIR CHOICE
                    else:
                        Request_New_Inputs.Request_New_Inputs()

    #FLAVOUR TEXT TO SYMBOLIZE THAT THE BATTLE WILL BEGIN
    else:
        print("The battle is inevitable!")
        Game_Loop = True

    #WILL WAIT FOR THE PLAYER'S INPUT BEFORE PROCEEDING TO ENSURE THAT HE HAD TIME TO READ 
    Wait_Input.Wait_Input()
    
    #CLEAR THE TERMINAL
    Clear_Screen.Clear_Screen()

    #INITIALIZE GAME LOOP
    while Game_Loop:

        #INCREASE THE TURN COUNT EVERY TURN AND PRINT IT
        Turn+=1
        print("TURN " + str(Turn))
        print("")
        
        #ORDER THE OBJECTS IN A LIST TO DETERMINE THE ORDER IN WHICH THEY ACT DURING THE TURN
        Ordered_Object_List = Turn_Order.Turn_Order(Priests_List, Warriors_List, OrcWarriors_List)
        print("")
        time.sleep(2)
        
        #PRINT THE ORDER IN A SIMPLER MANNER
        print("Order:")
        Counter = 0

        #ITERATE THROUGH THE OBJECT LIST
        for i in Ordered_Object_List:
            time.sleep(0.3)
            Counter += 1
            #PRINT THEM IN ORDER WHILE USING COUNTER TO NAME THEIR POSITION IN THE "QUEUE" TO ACT
            if isinstance(i, Warrior):
                print("   #" + str(Counter) + ": " + str(i.Name) + str(Warriors_List.index(i))) 
            elif isinstance(i, Priest):
                print("   #" + str(Counter) + ": " + str(i.Name) + str(Priests_List.index(i))) 
            else:
                print("   #" + str(Counter) + ": " + str(i.Name) + str(OrcWarriors_List.index(i)))
        print("")

        #PROGRAM WAITS FOR THE PLAYER'S INPUT TO ENSURE THAT THEY HAVE ENOUGH TIME TO READ ALL INFORMATION
        Wait_Input.Wait_Input()
        print("")

        #CLEAR THE SCREEN TO AVOID INFORMATION OVERLOAD
        Clear_Screen.Clear_Screen()

        
        #START OF COMBAT PHASE
        
        #ITERATE THROUGH THE LIST OF OBJECTS IN THE CORRECT ORDER
        for Unit in Ordered_Object_List:
            #IF THE INSTRUCTION TO BREAK THE LOOP HAS BEEN GIVEN (EVEN IF IT'S IN THE MIDDLE OF THE ACTION PHASE)
            if Game_Loop == False:
                #BREAK OUT OF THE LOOP
                break



            #IF THE OBJECT IS AN INSTANCE OF THE WARRIOR CLASS
            if isinstance(Unit,Warrior):
                
                #INITIATE THE CHOICE LOOP
                Choice = True
                while Choice == True:
                    
                    #PRINT THE STATS OF THE OBJECT IN QUESTION
                    print(str(Unit.Name) + str(Warriors_List.index(Unit)) + ":")
                    Print_Stats.Print_Stats(Unit)
                    print("1: ATTACK")
                    print("2: MAGIC")
                    print("")
                    print("What shall they do?")
                    
                    #RECEIVE THE INPUT
                    Action = input("> ")

                    #IF THE INPUT CORRESPONDS TO THE ATTACK OPTION
                    if Action == "1":

                        #START THE TARGETTING LOOP
                        while Choice == True:

                            #CLEAN THE TERMINAL TO AVOID INFORMATION OVERLOAD
                            Clear_Screen.Clear_Screen()

                            #PRINT THE STATS IMMEDIATELY AGAIN TO GIVE THE ILLUSION THAT ONLY THE LAST PART OF THE PREVIOUS INFORMATION WAS DELETED
                            print(str(Unit.Name) + str(Warriors_List.index(Unit)) + ":")
                            Print_Stats.Print_Stats(Unit)
                            print("ATTACK")
                            print("Please choose your Target:")

                            #PRINT EVERY AVAILABLE ENEMY TARGET WITH THEIR INDEX AND THEIR HEALTH SO THAT THE PLAYER CAN TARGET THEM ACCORDINGLY
                            for Enemy in OrcWarriors_List:
                                print("       " + str(OrcWarriors_List.index(Enemy)) + " - HP: " + str(Enemy.HP))
                            print("")

                            #RECEIVE THE INPUT OF THE TARGETTING
                            ChooseTarget = input("> ")
                            
                            #WILL TRY TO CONVERT THE INPUT INTO INT SO THAT IT CAN BE USED TO TARGET A SPECIFIC INDEX
                            try:

                                #CONVERT THE INPUT TO INT
                                ChooseTarget = int(ChooseTarget)

                                #IF THE INPUT CORRESPONDS TO THE INDEX OF AN OBJECT IN THE WARRIOR LIST
                                if ChooseTarget in range(len(OrcWarriors_List)):
                                
                                    #VARIABLE TARGET CORRESPONDS TO THE OBJECT WITH THE SELECTED INDEX
                                    Target = OrcWarriors_List[int(ChooseTarget)]
                                
                                    #THE TARGET'S HP IS DEDUCTED BY THE OBJECT'S WP SUBTRACTED WITH THE TARGET'S AP.
                                    Target.HP -= Unit.WP - Target.AP
                                
                                    #FLAVOUR TEXT
                                    print(Unit.Name + str(Warriors_List.index(Unit)) + " struck " + str(Target.Name) + str(OrcWarriors_List.index(Target)) +
                                    " for " + str(Unit.WP - Target.AP) + " damage!")
                                
                                    print(str(Target.Name) + str(OrcWarriors_List.index(Target)) + " has been left with " + str(Target.HP) + " HP.")
                                    
                                    #BREAK THE CHOICE LOOP
                                    Choice = False
                                
                                    #CHECK IF THE TARGET DIED DURING THIS ATTACK
                                    if Target.HP <= 0:
                                        print(str(Target.Name) + str(OrcWarriors_List.index(Target)) + " has died...")

                                        #IF YES, EMOVE THEM FROM THE LISTS SO THAT HE CANNOT BE TARGETTED, ATTACK NOR BE COUNTED FOR TURN ORDER
                                        OrcWarriors_List.remove(Target)
                                        Ordered_Object_List.remove(Target)
                                
                                #IF THE INPUT DOES NOT CORRESPOND TO THE INDEX OF ANY OBJECT IN THE WARRIOR LIST 
                                else:
                                    Request_New_Inputs.Request_New_Inputs()
                            
                            #IF THERE IS AN ERROR AS THE INPUT CANNOT BE CONVERTED INTO INT, INFORM THE PLAYER AND DO NOT BREAK THE LOOP SO THEY CAN TRY AGAIN
                            except:
                                Request_New_Inputs.Request_New_Inputs()
                        
                    #IF THE INPUT CORRESPONDS TO THE MAGIC ACTION
                    elif Action == "2":
                        
                        #START THE CHOICE LOOP
                        while Choice == True:

                            #CLEAR THE SCREEN TO AVOID INFORMATION OVERLOAD AND PRINT THE STATS
                            Clear_Screen.Clear_Screen()
                            print(str(Unit.Name) + str(Warriors_List.index(Unit)) + ":")
                            Print_Stats.Print_Stats(Unit)
                            
                            #PRINT THE AVAILABLE MAGIC OPTIONS
                            print("MAGIC")
                            print("Please choose your Spell:")
                            print("       1: Rushdown (5 MP) - Deals Warrior's WP + 4d Damage to a Selected Target")

                            #RECEIVE THE MAGIC INPUT
                            ChooseSpell = input(">")

                            #IF IT IS ONE OF THE MAGIC OPTIONS
                            if ChooseSpell == "1":

                                #ATTRIBUTE THE SPELL EFFECT AND THE MANA COST IN A LIST TO THIS VARIABLE
                                Damage_Cost = Unit.Rushdown()

                                #IF THE UNIT DOES NOT HAVE ENOUGH MANA TO CAST IT
                                if Unit.MP - Damage_Cost[1] < 0:

                                    #HE WILL FAIL TO DO SO AND LOSE HIS TURN
                                    print("The spell fails as there's not enough mana!")
                                    Unit.MP = 0

                                    #BREAK THE LOOP
                                    Choice = False

                                #IF THE UNIT DOES HAVE ENOUGH MANA TO CAST IT
                                else:

                                    #START ANOTHER CHOICE LOOP
                                    while Choice == True:

                                        #CLEAR THE SCREEN TO AVOID INFORMATION OVERLOAD AND PRINT THE STATS
                                        Clear_Screen.Clear_Screen()
                                        print(str(Unit.Name) + str(Warriors_List.index(Unit)) + ":")
                                        Print_Stats.Print_Stats(Unit)

                                        #PROMPT THE PLAYER TO SELECT THEIR TARGET
                                        print("MAGIC: Rushdown")
                                        print("Please choose your Target")

                                        #PRINT ALL THE ENEMIES IN THE LIST AND THEIR CORRESPONDING INDEX
                                        for Enemy in OrcWarriors_List:
                                            print("       " + str(OrcWarriors_List.index(Enemy)) + " - HP: " + str(Enemy.HP))
                                        print("")

                                        #RECEIVE THE TARGETTING INPUTS
                                        ChooseTarget = input("> ")
                                        
                                        #WILL TRY TO CONVERT IT INTO INT IN ORDER TO USE IT FOR THE INDEX
                                        try:
                                            
                                            #CONVERT THE INPUT INTO IT
                                            ChooseTarget = int(ChooseTarget)

                                            #IF THE INPUT IS A VALID INDEX FOR A TARGET
                                            if ChooseTarget in range(len(OrcWarriors_List)):
                                        
                                                #TARGET BECOMES THE OBJECT WHICH IS IN THE ENEMIES' LIST AT THE TARGET INDEX
                                                Target = OrcWarriors_List[int(ChooseTarget)]

                                                #TARGET'S HP GETS DEDUCTED THE SPELL EFFECT
                                                Target.HP += Damage_Cost[0]

                                                #THE UNIT'S MANA GETS DEDUCTED BY THE COST OF THE SPELL
                                                Unit.MP -= Damage_Cost[1]

                                                #FLAVOUR TEXT
                                                print(Unit.Name + str(Warriors_List.index(Unit)) + " rushed " + str(Target.Name) + str(OrcWarriors_List.index(Target)) +
                                                " with their sword for " + str(-Damage_Cost[0]) + " damage!")
                                        
                                                print(str(Target.Name) + str(OrcWarriors_List.index(Target)) + " has been left with " + str(Target.HP) + " HP.")
                                                
                                                #BREAK THE CHOICE LOOPS
                                                Choice = False
                                            
                                                #CHECK IF THE TARGET DIED DURING THIS ATTACK
                                                if Target.HP <= 0:
                                                    print(str(Target.Name) + str(OrcWarriors_List.index(Target)) + " has died...")
                                                    
                                                    #IF YES, REMOVE THEM FROM THE LISTS SO THAT HE CANNOT BE TARGETTED, CANNOT ACT THIS TURN AND DOES NOT COUNT FOR THE TURN ORDERS.
                                                    OrcWarriors_List.remove(Target)
                                                    Ordered_Object_List.remove(Target)

                                            #IF THE INPUT IS NOT A VALID INDEX FOR A TARGET
                                            else:
                                                #INFORM THE PLAYER AND REQUEST A NEW ONE
                                                Request_New_Inputs.Request_New_Inputs()

                                        #CATCH THE ERROR IF THE INPUT CANNOT BE CONVERTED INTO INT
                                        except:
                                            #INFORM THE PLAYER AND REQUEST A NEW ONE
                                            Request_New_Inputs.Request_New_Inputs()
                            
                            #IF THE INPUT IS NOT ONE OF THE MAGIC OPTIONS
                            else:
                                #INFORM THE PLAYER AND REQUEST A NEW INPUT 
                                Request_New_Inputs.Request_New_Inputs()
                    
                    #IF THE INPUT IS NEITHER THE OPTION FOR ATTACK OR FOR MAGIC
                    else:
                        #INFORM THE PLAYER AND REQUEST A NEW ONE
                        Request_New_Inputs.Request_New_Inputs()



            #IF THE OBJECT IS AN INSTANCE OF THE PRIEST CLASS
            elif isinstance(Unit,Priest):
                
                #INITIATE THE CHOICE LOOP
                Choice = True
                while Choice == True:
                    
                    #PRINT THE OBJECT'S STATS AND THE OPTIONS THEY MAY CHOOSE
                    print(str(Unit.Name) + str(Priests_List.index(Unit)) + ":")
                    Print_Stats.Print_Stats(Unit)
                    print("1: ATTACK")
                    print("2: MAGIC")
                    print("")
                    print("What shall they do?")
                    
                    #RECEIVE PLAYER INPUT 
                    Action = input("> ")

                    #IF THE INPUT CORRESPONDS TO THE ACTION VALUE
                    if Action == "1":

                        #INITIATE ANOTHER CHOICE LOOP
                        while Choice == True:

                            #CLEAR THE SCREEN
                            Clear_Screen.Clear_Screen()

                            #PRINT THE OBJECT'S STATS IMMEDIATELY TO PROVIDE THE ILLUSION THAT ONLY THE LAST FEW LINES WERE CLEARED
                            print(str(Unit.Name) + str(Priests_List.index(Unit)) + ":")
                            Print_Stats.Print_Stats(Unit)
                            print("ATTACK")
                            print("Please choose your Target:")
                            #PRINT EVERY ENEMY AVAILABLE AS WELL AS THE INDEX VALUE USED TO TARGET THEM
                            for Enemy in OrcWarriors_List:
                                print("       " + str(OrcWarriors_List.index(Enemy)) + " - HP: " + str(Enemy.HP))
                            print("")

                            #RECEIVE THE INPUT FOR THEIR DESIRED TARGET
                            ChooseTarget = input("> ")
                            
                            #WILL TRY TO CONVERT THE INPUT TO INT SO IT CAN BE USED TO TARGET A SPECIFIC INDEX
                            try:
                                #CONVERT THE INPUT TO THE CORRECT INDEX
                                ChooseTarget = int(ChooseTarget)

                                #IF THE INPUT CORRESPONDS TO THE INDEX OF A VALID ENEMY 
                                if ChooseTarget in range(len(OrcWarriors_List)):
                                    
                                    #ASSIGN THE TARGET TO THE CORRECT OBJECT
                                    Target = OrcWarriors_List[int(ChooseTarget)]
                                    
                                    #CALCULATE DAMAGE AND UPDATE IT TO THE TARGET'S HP
                                    Target.HP -= Unit.WP - Target.AP
                                    
                                    #FLAVOUR TEXT
                                    print(Unit.Name + str(Priests_List.index(Unit)) + " struck " + str(Target.Name) + str(OrcWarriors_List.index(Target)) +
                                    " for " + str(Unit.WP - Target.AP) + " damage!")
                                    
                                    print(str(Target.Name) + str(OrcWarriors_List.index(Target)) + " has been left with " + str(Target.HP) + " HP.")
                                    Choice = False
                                    
                                    #IF THE ACTION KILLED THE TARGET
                                    if Target.HP <= 0:
                                        print(str(Target.Name) + str(OrcWarriors_List.index(Target)) + " has died...")

                                        #REMOVE THEM FROM THE LISTS SO THAT THEY CANNOT ACT OR BE TARGETTED AS WELL AS NOT BE ABLE TO ACT THIS TURN 
                                        OrcWarriors_List.remove(Target)
                                        Ordered_Object_List.remove(Target)
                                
                                #IF THE INPUT DOES NOT CORRESPOND TO THE INDEX OF A VALID ENEMY
                                else:
                                    #INFORM THE PLAYER AND REQUEST A NEW ONE
                                    Request_New_Inputs.Request_New_Inputs()
                            
                            #CATCHES THE ERROR IF THE INPUT CANNOT BE CONVERTED TO INT
                            except:
                                #INFORM THE PLAYER AND REQUEST A NEW ONE
                                Request_New_Inputs.Request_New_Inputs()



                    #IF THE ACTION CORRESPONDS TO THE MAGIC ACTION
                    elif Action == "2":
                        
                        #INITIATE THE CHOICE LOOP
                        while Choice == True:

                            #PRINT THE OBJECT'S STATS AND THE OPTIONS THAT ARE AVAILABLE
                            Clear_Screen.Clear_Screen()
                            print(str(Unit.Name) + str(Priests_List.index(Unit)) + ":")
                            Print_Stats.Print_Stats(Unit)
                            print("MAGIC")
                            print("Please choose your Spell:")
                            print("       1: Exorcism (5 MP) - Deals d4 damage multiplied by 2 to Selected Target")
                            print("       2: Mend (3 MP) - Heals d6 + Priest's WP to Select Target.")

                            #RECEIVE CHOICE INPUT
                            ChooseSpell = input(">")
                            
                            #WILL TRY TO CONVERT THE CHOICE INPUT TO INT
                            try:
                                #CONVERT THE CHOICE INPUT TO INT SO THAT WE CAN UTILIZE IT TO ACCESS THE CORRECT INDEXES
                                ChooseSpell = int(ChooseSpell)

                                #IF THE CHOICE CORRESPONDS TO THE EXORCISM SPELL
                                if ChooseSpell == 1:

                                    #ASSIGNS THE SPELL EFFECT AND THE MANA COST VALUES FROM EXORCISM TO A LIST
                                    Damage_Cost = Unit.Exorcism()

                                    #IF THERE IS NOT ENOUGH MANA TO CAST THE SPELL
                                    if Unit.MP - Damage_Cost[1] < 0:
                                        print("The spell fails as there's not enough mana!")

                                        #REMOVE THE REMAINDER OF THE MANA AND LOSE THE ACTION
                                        Unit.MP = 0
                                        Choice = False

                                    #IF THERE IS ENOUGH MANA TO CAST THE SPELL
                                    else:

                                        #INITIATE THE CHOICE LOOP
                                        while Choice == True:
                                            Clear_Screen.Clear_Screen()

                                            #PRINT THE CHARACTER'S STATS AND THE OPTIONS THAT ARE AVAILABLE
                                            print(str(Unit.Name) + str(Priests_List.index(Unit)) + ":")
                                            Print_Stats.Print_Stats(Unit)
                                            print("MAGIC: Exorcism")
                                            print("Please choose your Target:")
                                            
                                            #PRINT ALL THE AVAILABLE TARGETS AND THEIR CORRESPONDING INDEX
                                            for Enemy in OrcWarriors_List:
                                                print("       " + str(OrcWarriors_List.index(Enemy)) + " - HP: " + str(Enemy.HP))
                                            print("")

                                            #RECEIVE THE PLAYER'S INPUT
                                            ChooseTarget = input("> ")
                                
                                            #WILL TRY TO CONVERT THE PLAYER'S INPUT TO AN INT
                                            try:

                                                #CONVERT THE PLAYER'S INPUT TO AN INT
                                                ChooseTarget = int(ChooseTarget)

                                                #IF THE INPUT IS A VALID INDEX FOR AN ENEMY
                                                if ChooseTarget in range(len(OrcWarriors_List)):
                                                    
                                                    #ASSIGN THE CORRESPONDING OBJECT TO THE TARGET VARIABLE
                                                    Target = OrcWarriors_List[int(ChooseTarget)]

                                                    #DEDUCT THE TARGET'S LIFE POINTS
                                                    Target.HP += Damage_Cost[0]

                                                    #DEDUCT THE UNIT'S MANA POINTS
                                                    Unit.MP -= Damage_Cost[1]

                                                    #FLAVOUR TEXT
                                                    print(Unit.Name + str(Priests_List.index(Unit)) + " exorcised " + str(Target.Name) + str(OrcWarriors_List.index(Target)) +
                                                    " for " + str(-Damage_Cost[0]) + " damage!")
                                            
                                                    print(str(Target.Name) + str(OrcWarriors_List.index(Target)) + " has been left with " + str(Target.HP) + " HP.")
                                                    Choice = False
                                            
                                                    #IF THE TARGET DIES FROM THIS ATTACK
                                                    if Target.HP <= 0:
                                                        print(str(Target.Name) + str(OrcWarriors_List.index(Target)) + " has died...")
                                                        
                                                        #REMOVE THEM FROM THE LISTS SO HE CANNOT ACT THIS TURN NOR BE TARGETTED OR BE TAKEN INTO ACCOUNT WHEN DECIDING THE TURN ORDER
                                                        OrcWarriors_List.remove(Target)
                                                        Ordered_Object_List.remove(Target)

                                                #IF THE INPUT IS NOT A VALID INDEX FOR AN ENEMY
                                                else:
                                                    Request_New_Inputs.Request_New_Inputs()
                                            #CATCHES THE ERROR IF THE PLAYER'S INPUT CANNOT BE CONVERTED INTO AN INT
                                            except:
                                                Request_New_Inputs.Request_New_Inputs()

                                #IF THE PLAYER'S INPUT CORRESPONDS TO THE MEND SPELL
                                elif ChooseSpell == 2:

                                            #ASSIGNS THE SPELL EFFECT AND THE MANA COST VALUES FROM MEND TO A LIST
                                            Damage_Cost = Unit.Mend()

                                            #IF THE UNIT DOES NOT HAVE ENOUGH MANA TO CAST THE SPELL
                                            if Unit.MP - Damage_Cost[1] < 0:
                                                print("The spell fails as there's not enough mana!")

                                                #REMOVES ALL OF THE UNIT'S REMAINING MANA POINTS AND HE LOSES THE ACTION 
                                                Unit.MP = 0
                                                Choice = False

                                            #IF THE UNIT HAS ENOUGH MANA TO CAST THE SPELL
                                            else:

                                                #INITIATE THE CHOICE LOOP
                                                while Choice == True:

                                                    #PRINT THE STATS AND THE AVAILABLE OPTIONS
                                                    Clear_Screen.Clear_Screen()
                                                    print(str(Unit.Name) + str(Priests_List.index(Unit)) + ":")
                                                    Print_Stats.Print_Stats(Unit)
                                                    print("MAGIC: Mend")
                                                    print("Please choose your Target")

                                                    #PRINT ALL THE AVAILABLE TARGETS (ALLIES) AND THE CORRESPONDING INDEXES
                                                    for Ally in Ally_List:
                                                        print("       " + str(Ally_List.index(Ally)) + " - HP: " + str(Ally.HP))
                                                    print("")

                                                    #RECEIVE THE CHOICE INPUT
                                                    ChooseTarget = input("> ")

                                                    #WILL TRY TO CONVERT THE CHOICE INPUT INTO INT
                                                    try:

                                                        #CONVERTS THE CHOICE INPUT INTO INT
                                                        ChooseTarget = int(ChooseTarget)

                                                        #IF THE CHOICE INPUT CORRESPONDS TO A VALID TARGET'S INDEX
                                                        if ChooseTarget in range(len(Ally_List)):
                                                    
                                                            #THE OBJECT TARGET IS ASSIGNED TO A TARGET VARIABLE
                                                            Target = Ally_List[int(ChooseTarget)]

                                                            #DEDUCTS THE SPELL'S SPELL EFFECT VALUE TO THE TARGET'S HP
                                                            Target.HP += Damage_Cost[0]

                                                            #DEDUCTS THE SPELL'S MANA COST TO THE UNIT'S MP
                                                            Unit.MP -= Damage_Cost[1]

                                                            #IF THE TARGET IS A WARRIOR
                                                            if Target in Warriors_List:

                                                                #INFORM THE PLAYER OF WHAT HAPPENED
                                                                print(Unit.Name + str(Priests_List.index(Unit)) + " healed a " + str(Target.Name) + str(Warriors_List.index(Target)) +
                                                                " for " + str(Damage_Cost[0]) + " health!")
                                                    
                                                                print(str(Target.Name) + str(Warriors_List.index(Target)) + " has been left with " + str(Target.HP) + " HP.")
                                                                
                                                                #BREAK THE LOOP
                                                                Choice = False

                                                            #IF THE TARGET IS A PRIEST
                                                            else:
                                                                #INFORM THE PLAYER OF WHAT HAPPENED
                                                                print(Unit.Name + str(Priests_List.index(Unit)) + " healed a " + str(Target.Name) + str(Priests_List.index(Target)) +
                                                                " for " + str(Damage_Cost[0]) + " health!")
                                                    
                                                                print(str(Target.Name) + str(Priests_List.index(Target)) + " has been left with " + str(Target.HP) + " HP.")
                                                                
                                                                #BREAK THE LOOP
                                                                Choice = False
                                                        
                                                        #IF THE CHOICE INPUT DOES NOT CORRESPOND TO A VALID TARGET'S INDEX
                                                        else:
                                                            Request_New_Inputs.Request_New_Inputs()

                                                    #IF THE CHOICE INPUT CANNOT BE CONVERTED INTO AN INT
                                                    except:
                                                        Request_New_Inputs.Request_New_Inputs()
                                
                                #IF THE PLAYER'S INPUT DOES NOT CORRESPOND TO ANY SPELL
                                else:
                                    Request_New_Inputs.Request_New_Inputs()

                            #IF THE CHOICE INPUT CANNOT BE CONVERTED INTO AN INT
                            except:
                                Request_New_Inputs.Request_New_Inputs()

                    #IF THE ACTION INPUT DOES NOT CORRESPOND TO ANY VALID ACTION
                    else:
                        Request_New_Inputs.Request_New_Inputs()



            #IF THE OBJECT IS AN INSTANCE OF THE ORC WARRIOR CLASS
            else:
                #RANDOMLY CHOOSE A TARGET FROM AMONG THE ADVENTURERS
                Target = (Ally_List)[random.randint(0,len(Ally_List)-1)]
                
                #CALCULATE THE DAMAGE AND REMOVE IT FROM THE TARGET'S CURRENT HP
                Target.HP -= Unit.WP - Target.AP
                
                #IF THE TARGET IS A PRIEST
                if Target in Priests_List:
                    #INFORM THE PLAYER OF WHAT HAPPENED
                    print(Unit.Name + str(OrcWarriors_List.index(Unit)) + " struck " + str(Target.Name) +
                    str(Priests_List.index(Target)) + " for " + str(Unit.WP - Target.AP) + " damage!")
                    print(str(Target.Name) + str(Priests_List.index(Target)) + " has been left with " + str(Target.HP) + " HP.")

                #IF THE TARGET IS AN ORC WARRIOR
                else:
                    #INFORM THE PLAYER OF WHAT HAPPENED
                    print(Unit.Name + str(OrcWarriors_List.index(Unit)) + " struck " + str(Target.Name) +
                    str(Warriors_List.index(Target)) + " for " + str(Unit.WP - Target.AP) + " damage!")  
                    print(str(Target.Name) + str(Warriors_List.index(Target)) + " has been left with " + str(Target.HP) + " HP.")  
                    
                #IF THE TARGET DIES FROM THE ATTACK
                if Target.HP <= 0:
                    #REMOVE THEM FROM THE ALLY LIST SO THAT THEY CANNOT BE ACT THIS TURN, BE TARGETTED OR CONSIDERED FOR TURN ORDER. 
                    Ally_List.remove(Target)
                    Ordered_Object_List.remove(Target)
                    
                    #IF THE TARGET IS A PRIEST
                    if Target.Name == "Priest_":
                        #INFORM THE PLAYER FROM WHAT HAPPENED AND REMOVE THEM FROM THE PRIESTS' LIST
                        print(str(Target.Name) + str(Priests_List.index(Target)) + "has died...")
                        Priests_List.remove(Target)
                    
                    #IF THE TARGET IS A WARRIOR
                    else:
                        #INFORM THE PLAYER OF WHAT HAPPENED AND REMOVE THEM FROM THE WARRIORS' LIST
                        print(str(Target.Name) + str(Warriors_List.index(Target)) + "has died...")
                        Warriors_List.remove(Target)
                        
            #WAITS FOR THE PLAYER'S INPUT TO PROGRESS INTO THE NEXT OBJECT'S ACTION PHASE AND CLEARS THE SCREEN TO AVOID INFORMATION OVERLOAD
            Wait_Input.Wait_Input()
            Clear_Screen.Clear_Screen()
            



            #CHECK IF THE PLAYER LOST (ALLIED LIST IS EMPTY AKA ALL ALLIES DIED)
            if Ally_List == []:
                
                #GIVES THE INSTRUCTION TO BREAK THE GAME LOOP
                Game_Loop = False
                
                #INITIATE CHOICE LOOP
                Choice = True
                while Choice == True:

                    #INFORM THE PLAYER THAT THEY LOST AND ASK IF THEY WANT TO REMATCH
                    Clear_Screen.Clear_Screen()
                    print("The Adventurers have been slaughtered...")
                    time.sleep(2)
                    print("Would you like a rematch? (y/n)")

                    #RECEIVE THE PLAYER'S INPUT
                    Rematch = input("> ")
                    
                    #IF THE PLAYER WANTS TO REMATCH, IT WILL EITHER PASS TO THE BEGINNING OF THE LOOP OR TO THE NEXT ITERATION OF THE FOR LOOP
                    #AND BREAK THE GAME LOOP
                    if Rematch.lower() == "y":
                        Choice = False
                        print("The battle shall restart.")
                        time.sleep(1)
                        print("Hope you have fun!")

                    #IF THE PLAYER DOES NOT WANT TO REMATCH, IT WILL EITHER PASS TO THE BEGINNING OF THE LOOP OR TO THE NEXT ITERATION OF THE FOR LOOP
                    #AND BREAK BOTH THE GAME AND THE MAIN LOOP, TERMINATING THE PROGRAM 
                    elif Rematch.lower() == "n":
                        Choice = False
                        Main_Loop = False
                        print("Thank you for playing!")
                        time.sleep(1)
                        print("Hope you had a good time!")
                    
                    #IF THE PLAYER PROVIDED AN INVALID INPUT
                    else:
                        Request_New_Inputs.Request_New_Inputs()
    
            #CHECK IF PLAYER WON (ORC WARRIOR IS EMPTY AKA ALL ENEMIES ARE DEAD):
            if OrcWarriors_List == []:
                
                #GIVE THE INSTRUCTION TO TERMINATE THE GAME LOOP
                Game_Loop = False

                #INFORM THE PLAYER THAT THEY WON AND ASK IF THEY WANT TO REMATCH
                Choice = True
                while Choice == True:
                    Clear_Screen.Clear_Screen()
                    print("The Orcs have been slain...")
                    time.sleep(2)
                    print("Would you like a rematch? (y/n)")
                    
                    #RECEIVE THE PLAYER'S INPUT
                    Rematch = input("> ")
                    
                    #IF THE PLAYER WANTS TO REMATCH, IT WILL EITHER PASS TO THE BEGINNING OF THE LOOP OR TO THE NEXT ITERATION OF THE FOR LOOP
                    #AND BREAK THE GAME LOOP
                    if Rematch.lower() == "y":
                        Choice = False
                        print("The battle shall restart.")
                        time.sleep(1)
                        print("Hope you have fun!")

                    #IF THE PLAYER DOES NOT WANT TO REMATCH, IT WILL EITHER PASS TO THE BEGINNING OF THE LOOP OR TO THE NEXT ITERATION OF THE FOR LOOP
                    #AND BREAK BOTH THE GAME AND THE MAIN LOOP, TERMINATING THE PROGRAM 
                    elif Rematch.lower() == "n":
                        Choice = False
                        Main_Loop = False
                        print("Thank you for playing!")
                        time.sleep(1)
                        print("Hope you had a good time!")
                    
                    #IF THE PLAYER PROVIDED AN INVALID INPUT
                    else:
                        Request_New_Inputs.Request_New_Inputs()