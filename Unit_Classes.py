#IMPORT RANDOM TO SIMULATE THE DICE ROLLS
import random

#DEFINING THE WARRIOR CLASS WITH THE DEFAULT VALUES AND ITS SPELLS
class Warrior():
    def __init__(self):
        self.Name = "Warrior_"
        self.HP = 32
        self.MP = 5
        self.AP = 2
        self.WP = 5
        self.Init = 2
    
    #DEFININING A METHOD FOR THE SPELL SO WE CAN CALL IT WHENEVER WE NEED
    def Rushdown(self):
        SpellEffectValue = -1 * (self.WP + random.randint(1,4))
        SpellMPCost = 5
        return (SpellEffectValue, SpellMPCost)

#DEFINING THE PRIEST CLASS WITH THE DEFAULT VALUES AND ITS SPELLS
class Priest():
    def __init__(self):
        self.Name = "Priest_"
        self.HP = 20
        self.MP = 25
        self.AP = 0
        self.WP = 2
        self.Init = 6
    
    #DEFININING A METHOD FOR THE SPELL SO WE CAN CALL IT WHENEVER WE NEED
    def Exorcism(self):
        SpellEffectValue = -1 * (random.randint(1,4) * 2)
        SpellMPCost = 5
        return (SpellEffectValue, SpellMPCost)
    
    #DEFININING A METHOD FOR THE SPELL SO WE CAN CALL IT WHENEVER WE NEED
    def Mend(self):
        SpellEffectValue = (random.randint(1,6) + self.WP)
        SpellMPCost = 3
        return (SpellEffectValue, SpellMPCost)

#DEFININING THE ENEMY'S CHARACTER CLASS WITH THE DEFAULT VALUES
class Orc_Warrior():
    def __init__(self):
        self.Name = "Orc Warrior_"
        self.HP = 15
        self.MP = 0
        self.AP = 2
        self.WP = 2
        self.Init = 2