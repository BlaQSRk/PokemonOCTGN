#------------------------------------------------------------------------------
# Global Values
#------------------------------------------------------------------------------

OldRules = True

#------------------------------------------------------------------------------
# Constant Values
#------------------------------------------------------------------------------

AttackColor = "#ff0000"
PokeBodyColor = "#74df00"
PokePowerColor = "#ffff00"

#------------------------------------------------------------------------------
# Markers
#------------------------------------------------------------------------------

BurnMarker = ("burn", "afd04701-8db9-4220-a38a-381e9c6b0e49")
PoisonMarker = ("poison", "54d7beba-c2aa-4ee8-973a-e8480a45b4da")
DamageMarker = ("damage", "9decdb60-fbd4-46bb-bf40-5f2bc5faeb68")
FaintMarker = ("faint", "4094170b-5d6f-4f79-8c75-1228cda7b3b3")
ToxicMarker = ("toxic", "28ca9176-a101-4697-9e41-ee1c43c2971c")

FireMarker = ("fire-elem","61b9a3f6-c897-4606-90af-3bad41dd5e98")
WaterMarker = ("water-elem", "deef855e-07a2-4496-b184-36060d23866f")
GrassMarker = ("grass-elem", "960b9c0b-2b25-4092-a1c9-6293b1520061")
LightningMarker = ("lightning-elem", "0b059eea-c344-486e-8162-21d2d6c11c87")
FightingMarker = ("fighting-elem", "f1781859-2d55-41b0-8e70-f343fe849a49")
PsychicMarker = ("psychic-elem", "75cf2b14-ba61-4601-ad7b-98e004bfc391")
FireResistMarker = ("fire-resist", "0d9b6b64-a0bf-4b09-a615-a5cff1644c4a")
WaterResistMarker = ("water-resist", "828bd2a0-60be-45b9-8475-f11554e1bca3")
GrassResistMarker = ("grass-resist", "880123d4-c288-44d9-b3b1-aebe4c789f81")
LightningResistMarker = ("lightning-resist", "9d36cf62-d9a8-40ae-b61c-8847516d03be")
FightingResistMarker = ("fighting-resist", "3df4a4a6-fd52-46b2-9b74-c6b05ba895b7")
PsychicResistMarker = ("psychic-resist", "0bcffdc6-7ece-437f-818d-99dea921bcc2")
FireWeakMarker = ("fire-weakness", "1deb3488-b7b6-4179-91ea-2bbba10f84b1")
WaterWeakMarker = ("water-weakness", "913b4d99-920d-426b-a8a1-e4703b690bcc")
GrassWeakMarker = ("grass-weakness", "c23d3df5-b8c2-4bc9-8e38-b8956814d06e")
LightningWeakMarker = ("lightning-weakness", "99a3d0ba-c86d-48a5-ae96-32f3e6b805c9")
FightingWeakMarker = ("fighting-weakness", "94a6319f-8dcc-4930-8d22-80febbbcfeda")
PsychicWeakMarker = ("psychic-weakness", "b9027080-75cd-4f3e-80f6-3a3d87de3698")

#------------------------------------------------------------------------------
# Table Actions
#------------------------------------------------------------------------------

def flipCoin(group, x = 0, y = 0):
    mute()
    n = rnd(1, 2)
    if n == 1:
        notify("{} flips heads.".format(me))
    else:
        notify("{} flips tails.".format(me))

def respond(group, x = 0, y = 0):
    notify('{} RESPONDS!'.format(me))

def turn(card, x = 0, y = 0):
    mute()
    if card.isFaceUp:
        notify("{} turns {} face down.".format(me, card))
        card.isFaceUp = False
    else:
        card.isFaceUp = True
        notify("{} turns {} face up.".format(me, card))

def pokepower(card, x = 0, y = 0):
    mute()
    name = card.PokePower
    if name == "0":
        notify("{} doesn't have a Poke-Power. Please select a valid option.".format(card))
    else:
        card.highlight = PokePowerColor
        notify("{} uses {}'s {}.".format(me, card, name))

def ability(card, x = 0, y = 0):
    mute()
    name = card.Ability
    if name == "0":
        notify("{} doesn't have an Ability. Please select a valid option.".format(card))
    else:
        card.highlight = PokePowerColor
        notify("{} uses {}'s {}.".format(me, card, name))

#----------------------------------------------------------------------------------
#def pokebody(card, x = 0, y = 0):
#    mute()
#    name = card.PokeBody
#    if name == "0":
#        notify("{} don't have a Poke-Body, select a valid option.".format(card))
#    else:
#        card.highlight = PokeBodyColor
#        notify("{} uses {}'s {}.".format(me, card, name))
#----------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Table Actions - Attacking Script
#------------------------------------------------------------------------------

#Unfinished
def atk(card, x = 0, y = 0):
    mute()
    
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    
    count = askInteger("Please select an Attack: 1, 2 or 3.",0)
    if count == 1:
        name = card.AtkName1
        if name == "0":
                notify("You can't make an attack with this card, you can only attack with a Pokemon")
        else: # Check For Status Effects
            if card.orientation == Rot90: #If Paralyzed, Do Nothing
                notify("{} is Paralyzed! It can't move!".format(card))
                if PoisonMarker in card.markers: #Debating Keeping these Status Checks. If its annoying, I'll remove them. 
                    poisonCheck(card, name)
                if BurnMarker in card.markers:
                    burnCheck(card,name)
            if card.orientation == Rot270:
                sleepCheck(card, name)
                if PoisonMarker in card.markers:
                    poisonCheck(card, name)
                if BurnMarker in card.markers:
                    burnCheck(card,name)
            elif card.orientation == Rot180:
                confuseCheck(card, name)
                if PoisonMarker in card.markers:
                    poisonCheck(card, name)
                if BurnMarker in card.markers:
                    burnCheck(card,name)
            else:
                card.highlight = AttackColor
                notify("{} attacks with {}'s {}.".format(me, card, name))
                if PoisonMarker in card.markers:
                    poisonCheck(card, name)
    elif count == 2:
        name = card.AtkName2
        if card.orientation == Rot180:
            confuseCheck(card, name)
        else:
            if name == "0":
                notify("{} doesn't have a second attack. Please select a valid option.".format(card))
            else:
                card.highlight = AttackColor
                notify("{} attacks with {}'s {}.".format(me, card, name))
                if PoisonMarker in card.markers:
                    poisonCheck(card, name)
    elif count == 3:
        name = card.AtkName3
        if card.orientation == Rot180:
            confuseCheck(card, name)
        else:
            if name == "0":
                notify("{} doesn't have a third attack. Please select a valid option.".format(card))
            else:
                card.highlight = AttackColor
                notify("{} attacks with {}'s {}.".format(me, card, name))
                if PoisonMarker in card.markers:
                    poisonCheck(card, name)
    else:
        notify("Please select a valid attack between 1 2 3 numbers.")

#---------------------------------------------
# Table Actions - Markers and Damage Markers
#---------------------------------------------

def addMarker(cards, x = 0, y = 0):
    mute()
    marker, quantity = askMarker()
    if quantity == 0: return
    for c in cards:
        c.markers[marker] += quantity
        if quantity == 1:
            notify("{} adds {} {} counter to {}.".format(me, quantity, marker[0], c))
        else:
            notify("{} adds {} {} counters to {}.".format(me, quantity, marker[0], c))
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

def addDamageMarker(card, x = 0, y = 0):
    mute()
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)
    
    # ---------------------- Damage Marker Code Starts Here ------
    HPcounter = int(card.HP)/10 #turn the card's HP into an integer and turns HPcounter into a damage counter value
    count = askInteger("How many damage counters will this pokemon take?",0)
    card.markers[DamageMarker] += count
    count2 = count*10
    notify("{} takes {} damage.".format(card, count2))
    if card.markers[DamageMarker] >= HPcounter: 
        card.markers[FaintMarker] += 1
        notify("{} has fainted. Please move it to the Discard Pile.".format(card))
    else: return

#Undone: Needs to be called in definition.xml as well.
def removeDamageMarker(card, x = 0, y = 0):
    mute()
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)
    
    # ---------------------- Damage Marker Code Starts Here ------
    HPcounter = int(card.HP)/10 #turn the card's HP into an integer and turns HPcounter into a damage counter value
    count = askInteger("How many damage counters will you remove from this Pokemon?",0)
    card.markers[DamageMarker] -= count
    if count >= 1:
        if card.markers[DamageMarker] == 0:
            notify("- {}'s HP was fully restored.".format(card))
        else:
            count2 = count*10
            notify(" - {}'s HP was restored for {} health.".format(card, count2))
    if card.markers[DamageMarker] < HPcounter: 
        card.markers[FaintMarker] = 0

# -----------------------------------------------
#  Table Actions - Status Effects - Card Rotation
# -----------------------------------------------

def addPoisonMarker(card, x = 0, y = 0):
    mute()
    card.markers[PoisonMarker] += 1
    notify("{} was Poisoned.".format(card))
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

def addToxicMarker(card, x = 0, y = 0):
    mute()
    if card.markers[PoisonMarker] >= 1:
        card.markers[PoisonMarker] = 0
    card.markers[ToxicMarker] += 1
    notify("{} was Badly Poisoned.".format(card))
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)
    
def addBurnMarker(card, x = 0, y = 0):
    mute()
    card.markers[BurnMarker] += 1
    notify("{} was Burned.".format(card))
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

def sleep(card, x = 0, y = 0):
    mute()
    card.orientation = Rot270
    notify("{} fell Asleep.".format(card))
    # --- Counter Update Code:
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

def confuse(card, x = 0, y = 0):
    mute()
    card.orientation = Rot180
    notify("{} became Confused.".format(card))
    # --- Counter Update Code:
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

def paralyze(card, x = 0, y = 0):
    mute()
    card.orientation = Rot90
    notify("{} is Paralyzed.".format(card))
    # --- Counter Update Code:
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

  
#------------------------------------------------------------------------------
# Table Actions - Status Checks and Heal
#------------------------------------------------------------------------------

def poisonCheck(card, x = 0, y = 0):
    mute()
    HPcounter = int(card.HP)/10 # Change card.HP into an int and HPcounter into a Damage-Counter value
    if PoisonMarker in card.markers:
        card.markers[DamageMarker] += 1
        notify("{} takes 10 damage from being Poisoned at end of the turn.".format(card))
        if card.markers[DamageMarker] >= HPcounter:
            card.markers[FaintMarker] += 1
            notify("{} has fainted. Please move it to the Discard Pile.".format(card))
        else: return
    else:
        notify("{} is not poisoned. Current action is not valid.".format(card))

def burnCheck(card, x = 0, y = 0):
    mute()
    HPcounter = int(card.HP)/10 # Change card.HP into an int and HPcounter into a Damage-Counter value
    n = rnd(1, 2)
    if BurnMarker in card.markers:
        if n == 1:
            notify("{} flips heads {} and doesn't take damage from being burned.".format(me, card))
        else:
            card.markers[DamageMarker] += 2
            notify("{} flips tails. {} takes 20 damage from being burned.".format(me, card))
            if card.markers[DamageMarker] >= HPcounter:
                card.markers[FaintMarker] += 1
                notify("{} has fainted. Please move it to the Discard Pile.".format(card))
            else: return
    else:
        notify("{} is not burned. Current action is not valid.".format(card))

def sleepCheck(card, x = 0, y = 0):
    mute()
    
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)
    # --- Counter Update Code Above
    
    n = rnd(1, 2)
    if card.orientation == Rot270:
        if n == 1:
            notify("{} woke up.".format(card))
            card.orientation = Rot0
        else:
            notify("{} is still sleeping.".format(card))
    else:
        notify("{} is not asleep. Current action is not valid.".format(card))

def confuseCheck(card, name, x = 0, y = 0):
    mute()
    
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)
    # --- Counter Update Code Above
    
    m = rnd(1, 2)      
    HPcounter = int(card.HP)/10 # Change card.HP into an int and  HPcounter into a Damage-Counter value
    if name == "0":
        notify("Select a valid Attack before attacking while Confused.")
    else:
        if m == 1:
            card.highlight = AttackColor
            notify("{} attacks normally with {}'s {} through its Confusion.".format(me, card, name))
        else:
            notify("{} hurt itself in Confusion for 20 damage.".format(card)) #Set as 20 Damage For the Earlier Decks I Use.
            card.markers[DamageMarker] += 2
            if card.markers[DamageMarker] >= HPcounter:
                card.markers[FaintMarker] += 1
                notify("{} fainted. Please move it to the Discard Pile.".format(card))
            else: return

def heal(card, x = 0, y = 0):
    mute()
    # Note: Code Needs to be reformatted into a For Loop In Order to Cure all ailments at once
    if PoisonMarker in card.markers:
        card.markers[PoisonMarker] = 0
        notify("{} is no longer Poisoned.".format(card))
        card.orientation = Rot0
    elif BurnMarker in card.markers:
        card.markers[BurnMarker] = 0
        notify("{} is no longer Burned.".format(card))        
    elif card.orientation == Rot90:
        card.orientation = Rot0
        notify("{} is no longer Paralyzed.".format(card))        
    elif card.orientation == Rot180:
        card.orientation = Rot0    
        notify("{} is no longer Confused.".format(card))
    elif card.orientation == Rot270:
        card.orientation = Rot0    
        notify("{} woke up.".format(card))
    else:
        notify("{} has no Status Ailments. Please select a valid option.".format(card))
    # --- Counter Update Code:
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

#------------------------------------------------------------------
# Table Actions - Discarding Cards and Deaths
#-------------------------------------------------------------------

def ko(card, x = 0, y = 0):
    mute()
    card.moveTo(me.piles['Discard Pile'])
    notify("{} discards {}.".format(me, card))
    # --- Counter Update Code:
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

def moveToLostZone(card, x = 0, y = 0):
    mute()
    card.moveTo(me.piles['Lost Zone'])
    notify("{} moves {} to the Lost Zone.".format(me, card))
    
    # --- Counter Update Code:
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

def clearAll(group, x = 0, y = 0):
    notify("{} clears all targets and combat.".format(me))
    for card in group:
      card.target(False)
      if card.controller == me and card.highlight in [AttackColor, PokeBodyColor, PokePowerColor]:
          card.highlight = None

# -----------------------------------------------
#  Markers - Elements
# -----------------------------------------------

def addFireMarker (card, x = 0, y = 0):
    mute()
    card.markers[FireMarker] += 1 #Add Fire Elemental Marker and Clears Any Other Elemental Marker
    if card.markers[WaterMarker] >= 1:
        card.markers[WaterMarker] = 0
    elif card.markers [GrassMarker] >=1:
        card.markers[GrassMarker] = 0
    elif card.markers [LightningMarker] >=1:
        card.markers[LightningMarker] = 0
    elif card.markers [FightingMarker] >=1:
        card.markers[FightingMarker] = 0
    elif card.markers [PsychicMarker] >=1:
        card.markers[PsychicMarker] = 0
    notify("{} is now a Fire Pokemon.".format(card))
        
def addWaterMarker (card, x = 0, y = 0):
    mute()
    card.markers[WaterMarker] += 1 #Add Water Elemental Marker and Clears Any Other Elemental Marker
    if card.markers[FireMarker] >= 1:
        card.markers[FireMarker] = 0
    elif card.markers [GrassMarker] >=1:
        card.markers[GrassMarker] = 0
    elif card.markers [LightningMarker] >=1:
        card.markers[LightningMarker] = 0
    elif card.markers [FightingMarker] >=1:
        card.markers[FightingMarker] = 0
    elif card.markers [PsychicMarker] >=1:
        card.markers[PsychicMarker] = 0
    notify("{} is now a Water Pokemon.".format(card))
    
def addGrassMarker (card, x = 0, y = 0):
    mute()
    card.markers[GrassMarker] += 1
    if card.markers[FireMarker] >= 1:
        card.markers[FireMarker] = 0
    elif card.markers [WaterMarker] >=1:
        card.markers[WaterMarker] = 0
    elif card.markers [LightningMarker] >=1:
        card.markers[LightningMarker] = 0
    elif card.markers [FightingMarker] >=1:
        card.markers[FightingMarker] = 0
    elif card.markers [PsychicMarker] >=1:
        card.markers[PsychicMarker] = 0
    notify("{} is now a Grass Pokemon.".format(card))

def addLightningMarker (card, x = 0, y = 0):
    mute()
    card.markers[LightningMarker] += 1
    if card.markers[FireMarker] >= 1:
        card.markers[FireMarker] = 0
    elif card.markers [WaterMarker] >=1:
        card.markers[WaterMarker] = 0
    elif card.markers [GrassMarker] >=1:
        card.markers[GrassMarker] = 0
    elif card.markers [FightingMarker] >=1:
        card.markers[FightingMarker] = 0
    elif card.markers [PsychicMarker] >=1:
        card.markers[PsychicMarker] = 0
    notify("{} is now a Lightning Pokemon.".format(card))
    
def addFightingMarker (card, x = 0, y = 0):
    mute()
    card.markers[FightingMarker] += 1
    if card.markers[FireMarker] >= 1:
        card.markers[FireMarker] = 0
    elif card.markers [WaterMarker] >=1:
        card.markers[WaterMarker] = 0
    elif card.markers [LightningMarker] >=1:
        card.markers[LightningMarker] = 0
    elif card.markers [GrassMarker] >=1:
        card.markers[GrassMarker] = 0
    elif card.markers [PsychicMarker] >=1:
        card.markers[PsychicMarker] = 0
    notify("{} is now a Fighting Pokemon.".format(card))
    
def addPsychicMarker (card, x = 0, y = 0):
    mute()
    card.markers[PsychicMarker] += 1
    if card.markers[FireMarker] >= 1:
        card.markers[FireMarker] = 0
    elif card.markers [WaterMarker] >=1:
        card.markers[WaterMarker] = 0
    elif card.markers [LightningMarker] >=1:
        card.markers[LightningMarker] = 0
    elif card.markers [FightingMarker] >=1:
        card.markers[FightingMarker] = 0
    elif card.markers [GrassMarker] >=1:
        card.markers[GrassMarker] = 0
    notify("{} is now a Psychic Pokemon.".format(card))
    
# -----------------------------------------------
#  Markers - Weaknesses
# -----------------------------------------------

def addFireWeakMarker (card, x = 0, y = 0):
    mute()
    card.markers[FireWeakMarker] += 1
    if card.markers[WaterWeakMarker] >= 1:
        card.markers[WaterWeakMarker] = 0
    elif card.markers [GrassWeakMarker] >=1:
        card.markers[GrassWeakMarker] = 0
    elif card.markers [LightningWeakMarker] >=1:
        card.markers[LightningWeakMarker] = 0
    elif card.markers [FightingWeakMarker] >=1:
        card.markers[FightingWeakMarker] = 0
    elif card.markers [PsychicWeakMarker] >=1:
        card.markers[PsychicWeakMarker] = 0
    notify("{} now has a Weakness to the Fire Element.".format(card))
        
def addWaterWeakMarker (card, x = 0, y = 0):
    mute()
    card.markers[WaterWeakMarker] += 1
    if card.markers[FireWeakMarker] >= 1:
        card.markers[FireWeakMarker] = 0
    elif card.markers [GrassWeakMarker] >=1:
        card.markers[GrassWeakMarker] = 0
    elif card.markers [LightningWeakMarker] >=1:
        card.markers[LightningWeakMarker] = 0
    elif card.markers [FightingWeakMarker] >=1:
        card.markers[FightingWeakMarker] = 0
    elif card.markers [PsychicWeakMarker] >=1:
        card.markers[PsychicWeakMarker] = 0
    notify("{} now has a Weakness to the Water Element.".format(card))
    
def addGrassWeakMarker (card, x = 0, y = 0):
    mute()
    card.markers[GrassWeakMarker] += 1
    if card.markers[FireWeakMarker] >= 1:
        card.markers[FireWeakMarker] = 0
    elif card.markers [WaterWeakMarker] >=1:
        card.markers[WaterWeakMarker] = 0
    elif card.markers [LightningWeakMarker] >=1:
        card.markers[LightningWeakMarker] = 0
    elif card.markers [FightingWeakMarker] >=1:
        card.markers[FightingWeakMarker] = 0
    elif card.markers [PsychicWeakMarker] >=1:
        card.markers[PsychicWeakMarker] = 0
    notify("{} now has a Weakness to the Grass Element.".format(card))

def addLightningWeakMarker (card, x = 0, y = 0):
    mute()
    card.markers[LightningWeakMarker] += 1
    if card.markers[FireWeakMarker] >= 1:
        card.markers[FireWeakMarker] = 0
    elif card.markers [WaterWeakMarker] >=1:
        card.markers[WaterWeakMarker] = 0
    elif card.markers [GrassWeakMarker] >=1:
        card.markers[GrassWeakMarker] = 0
    elif card.markers [FightingWeakMarker] >=1:
        card.markers[FightingWeakMarker] = 0
    elif card.markers [PsychicWeakMarker] >=1:
        card.markers[PsychicWeakMarker] = 0
    notify("{} now has a Weakness to the Lightning Element.".format(card))
    
def addFightingWeakMarker (card, x = 0, y = 0):
    mute()
    card.markers[FightingWeakMarker] += 1
    if card.markers[FireWeakMarker] >= 1:
        card.markers[FireWeakMarker] = 0
    elif card.markers [WaterWeakMarker] >=1:
        card.markers[WaterWeakMarker] = 0
    elif card.markers [LightningWeakMarker] >=1:
        card.markers[LightningWeakMarker] = 0
    elif card.markers [GrassWeakMarker] >=1:
        card.markers[GrassWeakMarker] = 0
    elif card.markers [PsychicWeakMarker] >=1:
        card.markers[PsychicWeakMarker] = 0
    notify("{} now has a Weakness to the Fighting Element.".format(card))
    
def addPsychicWeakMarker (card, x = 0, y = 0):
    mute()
    card.markers[PsychicWeakMarker] += 1
    if card.markers[FireWeakMarker] >= 1:
        card.markers[FireWeakMarker] = 0
    elif card.markers [WaterWeakMarker] >=1:
        card.markers[WaterWeakMarker] = 0
    elif card.markers [LightningWeakMarker] >=1:
        card.markers[LightningWeakMarker] = 0
    elif card.markers [FightingWeakMarker] >=1:
        card.markers[FightingWeakMarker] = 0
    elif card.markers [GrassWeakMarker] >=1:
        card.markers[GrassWeakMarker] = 0
    notify("{} now has a Weakness to the Psychic Element.".format(card))

# -----------------------------------------------
#  Markers - Resistance
# -----------------------------------------------
def addFireResistMarker (card, x = 0, y = 0):
    mute()
    card.markers[FireResistMarker] += 1
    if card.markers[WaterResistMarker] >= 1:
        card.markers[WaterResistMarker] = 0
    elif card.markers [GrassResistMarker] >=1:
        card.markers[GrassResistMarker] = 0
    elif card.markers [LightningResistMarker] >=1:
        card.markers[LightningResistMarker] = 0
    elif card.markers [FightingResistMarker] >=1:
        card.markers[FightingResistMarker] = 0
    elif card.markers [PsychicResistMarker] >=1:
        card.markers[PsychicResistMarker] = 0
    notify("{} now has Resistance against the Fire Element.".format(card))
        
def addWaterResistMarker (card, x = 0, y = 0):
    mute()
    card.markers[WaterResistMarker] += 1
    if card.markers[FireResistMarker] >= 1:
        card.markers[FireResistMarker] = 0
    elif card.markers [GrassResistMarker] >=1:
        card.markers[GrassResistMarker] = 0
    elif card.markers [LightningResistMarker] >=1:
        card.markers[LightningResistMarker] = 0
    elif card.markers [FightingResistMarker] >=1:
        card.markers[FightingResistMarker] = 0
    elif card.markers [PsychicResistMarker] >=1:
        card.markers[PsychicResistMarker] = 0
    notify("{} now has Resistance against the Water Element.".format(card))
    
def addGrassResistMarker (card, x = 0, y = 0):
    mute()
    card.markers[GrassResistMarker] += 1
    if card.markers[FireResistMarker] >= 1:
        card.markers[FireResistMarker] = 0
    elif card.markers [WaterResistMarker] >=1:
        card.markers[WaterResistMarker] = 0
    elif card.markers [LightningResistMarker] >=1:
        card.markers[LightningResistMarker] = 0
    elif card.markers [FightingResistMarker] >=1:
        card.markers[FightingResistMarker] = 0
    elif card.markers [PsychicResistMarker] >=1:
        card.markers[PsychicResistMarker] = 0
    notify("{} now has Resistance against the Grass Element.".format(card))

def addLightningResistMarker (card, x = 0, y = 0):
    mute()
    card.markers[LightningResistMarker] += 1
    if card.markers[FireResistMarker] >= 1:
        card.markers[FireResistMarker] = 0
    elif card.markers [WaterResistMarker] >=1:
        card.markers[WaterResistMarker] = 0
    elif card.markers [GrassResistMarker] >=1:
        card.markers[GrassResistMarker] = 0
    elif card.markers [FightingResistMarker] >=1:
        card.markers[FightingResistMarker] = 0
    elif card.markers [PsychicResistMarker] >=1:
        card.markers[PsychicResistMarker] = 0
    notify("{} now has Resistance against the Lightning Element.".format(card))
    
def addFightingResistMarker (card, x = 0, y = 0):
    mute()
    card.markers[FightingResistMarker] += 1
    if card.markers[FireResistMarker] >= 1:
        card.markers[FireResistMarker] = 0
    elif card.markers [WaterResistMarker] >=1:
        card.markers[WaterResistMarker] = 0
    elif card.markers [LightningResistMarker] >=1:
        card.markers[LightningResistMarker] = 0
    elif card.markers [GrassResistMarker] >=1:
        card.markers[GrassResistMarker] = 0
    elif card.markers [PsychicResistMarker] >=1:
        card.markers[PsychicResistMarker] = 0
    notify("{} now has Resistance against the Fighting Element.".format(card))
    
def addPsychicResistMarker (card, x = 0, y = 0):
    mute()
    card.markers[PsychicResistMarker] += 1
    if card.markers[FireResistMarker] >= 1:
        card.markers[FireResistMarker] = 0
    elif card.markers [WaterResistMarker] >=1:
        card.markers[WaterResistMarker] = 0
    elif card.markers [LightningResistMarker] >=1:
        card.markers[LightningResistMarker] = 0
    elif card.markers [FightingResistMarker] >=1:
        card.markers[FightingResistMarker] = 0
    elif card.markers [GrassResistMarker] >=1:
        card.markers[GrassResistMarker] = 0
    notify("{} now has Resistance against the Psychic Element.".format(card))

#------------------------------------------------------------------------------
# Hand Actions
#------------------------------------------------------------------------------

def playFaceDown(card, x = 0, y = 0):
    mute()
    card.moveToTable(0, 0, True)
    notify("{} set a card face-down on the field.".format(me))
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

def discard(card, x = 0, y = 0):
    mute()
    notify("{} discards {} from their hand.".format(me, card))
    card.moveTo(me.piles['Discard Pile'])
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

def moveToLostZoneHand(card, x = 0, y = 0):
    mute()
    notify("{} moved {} from their hand to the Lost Zone.".format(me, card))
    card.moveTo(me.piles['Lost Zone'])
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

def randomDiscard(group, x = 0, y = 0):
    mute()
    card = group.random()
    if card == None: return
    notify("{} randomly discards a card.".format(me))
    card.moveTo(me.piles['Discard Pile'])
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

def mulligan(group):
    mute()
    for card in group:
        card.moveTo(me.piles['Deck'])
    me.piles['Deck'].shuffle()
    for card in me.piles['Deck'].top(7):
        card.moveTo(me.hand)
    notify("{} mulligans, opponents may draw an extra card.".format(me))
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

#------------------------------------------------------------------------------
# Deck Actions
#------------------------------------------------------------------------------

def draw(group, x = 0, y = 0):
    if len(group) == 0: return
    mute()
    group[0].moveTo(me.hand)
    notify("{} draws a card.".format(me))
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

def drawMany(group, count = None):
    if len(group) == 0: return
    mute()
    if count == None: count = askInteger("Draw how many cards?", 7)
    for c in group.top(count): c.moveTo(me.hand)
    
    notify("{} draws {} cards.".format(me, count))
    
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

def mill(group, count = None):
    if len(group) == 0: return
    mute()
    if count == None: count = askInteger("Mill how many cards?", 1)
    for c in group.top(count): c.moveTo(me.piles['Discard Pile'])
    notify("{} sends the top {} cards from their Deck to the Discard Pile.".format(me, count))
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

def sendToLostZone(group, count = None):
    if len(group) == 0: return
    mute()
    if count == None: count = askInteger("Mill how many cards?", 1)
    for c in group.top(count): c.moveTo(me.piles['Lost Zone'])
    notify("{} sends the top {} cards from their Deck to the Lost Zone.".format(me, count))
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

def shuffle(group):
    group.shuffle()
    notify("{} shuffled their deck".format(me))
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

def setPrizes(group):
    if len(group) == 0: return
    mute()
    for c in group.top(6): c.moveTo(me.piles['Prizes Zone'])
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    notify("{} sets their prizes".format(me))
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)

#------------------------------------------------------------------------------
# Prize Zone Actions
#------------------------------------------------------------------------------

def claimPrize(group, x = 0, y = 0):
    mute()
    if len(group) == 0:
        notify("There are no prizes to claim. Current action is not valid.") 
        return
    group[0].moveTo(me.hand)
    notify("{} claims a prize card.".format(me))
    me.PrizeCount = len(group) # Updates Prize Card Count Marker
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)
    if len(group) == 0:
        notify("Congratulations! {} has claimed all of their prizes and has won the game!".format(me))
    else: return

def shufflePrizeCards(group):
    group.shuffle()
    notify("{} shuffled their prize cards".format(me))
    me.PrizeCount = len(me.piles['Prizes Zone']) # Updates Prize Card Count (Just For Some Common Actions)
    me.HandCount = len(me.hand) # Updates Hand Card Count (Just For Some Common Actions)
