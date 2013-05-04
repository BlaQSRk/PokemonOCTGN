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
        notify("{} don't have a Poke-Power, select a valid option.".format(card))
    else:
        card.highlight = PokePowerColor
        notify("{} uses {}'s {}.".format(me, card, name))

def ability(card, x = 0, y = 0):
    mute()
    name = card.Ability
    if name == "0":
        notify("{} don't have an Ability, select a valid option.".format(card))
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

def addMarker(cards, x = 0, y = 0):
    mute()
    marker, quantity = askMarker()
    if quantity == 0: return
    for c in cards:
        c.markers[marker] += quantity
        notify("{} adds {} {} counter to {}.".format(me, quantity, marker[0], c))

def addPoisonMarker(card, x = 0, y = 0):
    mute()
    card.markers[PoisonMarker] += 1
    notify("{} is now Poisoned.".format(card))
    
def addBurnMarker(card, x = 0, y = 0):
    mute()
    card.markers[BurnMarker] += 1
    notify("{} is now Burned.".format(card))

def addDamageMarker(card, x = 0, y = 0):
    mute()
    HPnew = (card.HP) / 10
    count = askInteger("How many damage counters will this pokemon take?",0)
    card.markers[DamageMarker] += count
    count2 = count*10
    notify("{} takes {} of damage.".format(card, count2))
    if card.markers[DamageMarker] >= HPnew:
        card.markers[FaintMarker] += 1
        notify("{} fainted, please move it to the Discard Pile.".format(card))
    else: return

def sleep(card, x = 0, y = 0):
    mute()
    card.orientation = Rot270
    notify("{} is now asleep.".format(card))

def confuse(card, x = 0, y = 0):
    mute()
    card.orientation = Rot180
    notify("{} is now confused.".format(card))

def paralyze(card, x = 0, y = 0):
    mute()
    card.orientation = Rot90
    notify("{} is now paralyzed.".format(card))

def heal(card, x = 0, y = 0):
    mute()
    card.orientation = Rot0
    notify("{} Special Condition is removed.".format(card))
    if PoisonMarker in card.markers:
        card.markers[PoisonMarker] -= 1
    elif BurnMarker in card.markers:
        card.markers[BurnMarker] -= 1

def poisonCheck(card, x = 0, y = 0):
    mute()
    HPnew = card.HP/10
    if PoisonMarker in card.markers:
        card.markers[DamageMarker] += 1
        notify("{} takes 10 of damage from being poisoned at end of turn.".format(card))
        if card.markers[DamageMarker] >= HPnew:
            card.markers[FaintMarker] += 1
            notify("{} fainted, please move it to the Discard Pile.".format(card))
        else: return
    else:
        notify("{} is not poisoned, current action is not valid.".format(card))

def burnCheck(card, x = 0, y = 0):
    mute()
    HPnew = card.HP/10
    n = rnd(1, 2)
    if BurnMarker in card.markers:
        if n == 1:
            notify("{} flips head {} don't take damage from being burned.".format(me, card))
        else:
            card.markers[DamageMarker] += 2
            notify("{} flips tails {} takes 20 of damage from being burned.".format(me, card))
            if card.markers[DamageMarker] >= HPnew:
                card.markers[FaintMarker] += 1
                notify("{} fainted, please move it to the Discard Pile.".format(card))
            else: return
    else:
        notify("{} is not burned, current action is not valid.".format(card))

def sleepCheck(card, x = 0, y = 0):
    mute()
    n = rnd(1, 2)
    if card.orientation == Rot270:
        if n == 1:
            notify("{} woke up.".format(card))
            card.orientation = Rot0
        else:
            notify("{} is still sleeping.".format(card))
    else:
        notify("{} is not asleep, current action is not valid.".format(card))

def confuseCheck(card, name):
    mute()
    m = rnd(1, 2)
    HPnew = card.HP/10
    if name == "0":
        notify("Select a valid Attack before attacking in a confuse condition.")
    else:
        if m == 1:
            card.highlight = AttackColor
            notify("{} attacks normally with {}'s {} through the confusion condition.".format(me, card, name))
        else:
            notify("{} flips tails and {} takes 30 of damage due to confusion.".format(me, card))
            card.markers[DamageMarker] += 3
            if card.markers[DamageMarker] >= HPnew:
                card.markers[FaintMarker] += 1
                notify("{} fainted, please move it to the Discard Pile.".format(card))
            else: return

def ko(card, x = 0, y = 0):
    mute()
    card.moveTo(me.piles['Discard Pile'])
    notify("{} discards {}.".format(me, card))

def moveToLostZone(card, x = 0, y = 0):
    mute()
    card.moveTo(me.piles['Lost Zone'])
    notify("{} moves {} to the Lost Zone.".format(me, card))

def clearAll(group, x = 0, y = 0):
    notify("{} clears all targets and combat.".format(me))
    for card in group:
      card.target(False)
      if card.controller == me and card.highlight in [AttackColor, PokeBodyColor, PokePowerColor]:
          card.highlight = None

def atk(card, x = 0, y = 0):
    mute()
    count = askInteger("Please select an Attack: 1, 2 or 3.",0)
    if count == 1:
        name = card.AtkName1
        if card.orientation == Rot180:
            confuseCheck(card, name)
        else:
            if name == "0":
                notify("You can't make an attack with this card, you can only attack with a Pokemon")
            else:
                card.highlight = AttackColor
                notify("{} attacks with {}'s {}.".format(me, card, name))
    elif count == 2:
        name = card.AtkName2
        if card.orientation == Rot180:
            confuseCheck(card, name)
        else:
            if name == "0":
                notify("{} don't have a second attack, select a valid option.".format(card))
            else:
                card.highlight = AttackColor
                notify("{} attacks with {}'s {}.".format(me, card, name))
    elif count == 3:
        name = card.AtkName3
        if card.orientation == Rot180:
            confuseCheck(card, name)
        else:
            if name == "0":
                notify("{} don't have a third attack, select a valid option.".format(card))
            else:
                card.highlight = AttackColor
                notify("{} attacks with {}'s {}.".format(me, card, name))
    else:
        notify("Please select a valid attack between 1 2 3 numbers.")

#------------------------------------------------------------------------------
# Hand Actions
#------------------------------------------------------------------------------

def playFaceDown(card, x = 0, y = 0):
    mute()
    card.moveToTable(0, 0, True)
    notify("{} set a card on the field.".format(me))

def discard(card, x = 0, y = 0):
    mute()
    notify("{} discards {} from their hand.".format(me, card))
    card.moveTo(me.piles['Discard Pile'])

def moveToLostZone(card, x = 0, y = 0):
    mute()
    notify("{} moved {} from their hand to the Lost Zone.".format(me, card))
    card.moveTo(me.piles['Lost Zone'])

def randomDiscard(group, x = 0, y = 0):
    mute()
    card = group.random()
    if card == None: return
    notify("{} randomly discards a card.".format(me))
    card.moveTo(me.piles['Discard Pile'])

def mulligan(group):
    mute()
    for card in group:
        card.moveTo(me.piles['Deck'])
    me.piles['Deck'].shuffle()
    for card in me.piles['Deck'].top(7):
        card.moveTo(me.hand)
    notify("{} mulligans, opponents may draw an extra card.".format(me))

#------------------------------------------------------------------------------
# Deck Actions
#------------------------------------------------------------------------------

def draw(group, x = 0, y = 0):
    if len(group) == 0: return
    mute()
    group[0].moveTo(me.hand)
    notify("{} draws a card.".format(me))

def drawMany(group, count = None):
    if len(group) == 0: return
    mute()
    if count == None: count = askInteger("Draw how many cards?", 7)
    for c in group.top(count): c.moveTo(me.hand)
    notify("{} draws {} cards.".format(me, count))

def mill(group, count = None):
    if len(group) == 0: return
    mute()
    if count == None: count = askInteger("Mill how many cards?", 1)
    for c in group.top(count): c.moveTo(me.piles['Discard Pile'])
    notify("{} sends the top {} cards from his Deck to the Discard Pile.".format(me, count))

def sendToLostZone(group, count = None):
    if len(group) == 0: return
    mute()
    if count == None: count = askInteger("Mill how many cards?", 1)
    for c in group.top(count): c.moveTo(me.piles['Lost Zone'])
    notify("{} sends the top {} cards from his Deck to the Lost Zone.".format(me, count))

def shuffle(group):
    group.shuffle()
    notify("{} shuffled his deck".format(me))

def setPrizes(group):
    if len(group) == 0: return
    mute()
    for c in group.top(6): c.moveTo(me.piles['Prizes Zone'])
    notify("{} set his prizes".format(me))

#------------------------------------------------------------------------------
# Prize Zone Actions
#------------------------------------------------------------------------------

def claimPrize(group, x = 0, y = 0):
    mute()
    if len(group) == 0: return
    group[0].moveTo(me.hand)
    notify("{} claims a prize card.".format(me))

def shufflePrizeCards(group):
    group.shuffle()
    notify("{} shuffled his prize cards".format(me))
