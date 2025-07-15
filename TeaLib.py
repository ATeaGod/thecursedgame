from encounters import * 
import random
import time
### Utils ###
def clsc():
    print('\033[H\033[J')

### Questing ###
charname = ""

def startup():
    clsc()
    global charname
    print("Welcome To This Game","\n1: Load Save","\n2: New Save")
    enter = int(input(">> "))
    if enter == 1:
        clsc()
        print("Choose Save Slot 1-3")
        savenum = int(input(">> "))
    if enter == 2:
        clsc()
        print("Make New Save Choose 1-3")
        savenum = int(input(">> "))
        print("What is thy name?")
        charname = input(">> ")
    else:
        print("Blehhhh")
    clsc()


health = 20
inventory = ["placeholder1", "placeholder2", "placeholder3"]
def options():
    print(charname, "you have,", health, "health and", len(inventory), "Items.")
    print("1: inventory      3: Check Exp","\n2: attack")
    selection = int(input(">>>"))
    if selection == 1:
        inverntorymenu()
    if selection == 2:
        encounter()
    if selection == 3:
        playstats()
def listinv():
    for i in range(len(inventory)):
         print(inventory[i])
         print("")
def inverntorymenu():
    while True:
        clsc()
        print("1: check items","\n2: use item","\n3: craft item","\n4: go back")
        selection = int(input(">>>"))
        if selection == 1:
            print("In your inventory there is", len(inventory), "items: ")
            print("")
            listinv()
            print("\n1: Go Back")
            input(">>> ")
        if selection == 2:
            print("placeholder")
        if selection == 3:
            print("placeholder")
        if selection == 4:
            print("Headed Back To Menu")
            break


def wildcardcheck():
    iswildcard = random.randint(0, 1000)
    if iswildcard == 55:
        wildcard = True
    else:
        wildcard = False
    return wildcard
def zombie(lvl):
    wildcard = wildcardcheck()
    clsc()
    global mhealth, defence, damage
    if wildcard == True:
        mhealth = random.randint(1, 100)
        defence = random.randint(0, 19)
        damage = random.randint(0, 20)
    else:
        ranges = {
            0:  ((1, 3),  (0, 2), (0, 2)),
            1:  ((1, 5),   (0, 4), (0, 3)),
            2:  ((3, 8),  (1, 4), (1, 5)),
            3:  ((6, 8),  (1, 4), (1, 5)),
            4:  ((8, 9),  (4, 4), (1, 6)),
            5:  ((8, 11), (8,10), (2, 6)),
            6:  ((9, 13), (2,10), (1,8)),
            7:  ((11, 15), (4, 10), (3, 8)),
            8:  ((13, 20), (5, 12), (2, 9)),
            9:  ((15, 20), (5, 12), (4, 10)),
            10:  ((20, 30), (7, 15), (3, 13)),
        }
        health_rng, def_rng, dmg_rng = ranges.get(lvl, ((1, 1), (0, 0), (0,0,)))
        mhealth = random.randint(*health_rng)
        defence = random.randint(*def_rng)
        damage = random.randint(*dmg_rng)
    print(f"This Zombie has {mhealth} Health and {defence} Defence.")
    contimue()
def skeleton(lvl):
    wildcard = wildcardcheck()
    clsc()
    global mhealth, defence, damage
    if wildcard == True:
        mhealth = random.randint(1, 50)
        defence = random.randint(1, 10)
        damage = random.randint(1, 30)
    else:
        ranges = {
            0: ((1, 2), (0, 1), (1, 3)),
            1: ((1, 3), (0, 1), (2, 5)),
            2: ((1, 4), (0, 2), (2, 6)),
            3: ((1, 4), (0, 2), (3, 6)),
            4: ((2, 4), (0, 3), (3, 8)),
            5: ((2, 5), (0, 3), (1, 12)),
            6: ((2, 6), (0, 4), (5, 10)),
            7: ((2, 7), (0, 4), (5, 11)),
            8: ((2, 7), (0, 5), (6, 9)),
            9: ((2, 7), (0, 5), (7, 10)),
            10: ((2, 10), (5, 10), (8, 18)),
        }
        health_rng, def_rng, dmg_rng = ranges.get(lvl, ((1, 1), (0, 1), (1, 3)))
        mhealth = random.randint(*health_rng)
        defence = random.randint(*def_rng)
        damage = random.randint(*dmg_rng)
        print(f"This Skeleton has {mhealth} health and {defence} Defence.")
        contimue()
### Encounters & Levels ###
def missenc():
    clsc()
    print("\nyou missed!, they decide to fight back!")
    print("\nroll a D12 to deflect!")
    input(">>> ")
    roll = sir(12)
    if roll <= 10:
        print("The zombie dealt", damage,"Damage!")
        guh = damage - (damage * 2)
        hc(guh)
    else:
       print("You Deflected The Hit!")
       if health <= 0:
           ded()
           quit()
    time.sleep(1)
    clsc()

def hmissenc(dmgammnt):
    global health, mhealth, damage
    print("The creature took", dmgammnt,"damage.")
    mhealth = mhealth - dmgammnt
    print("\nyou didnt kill the enemy, they decide to fight back!")
    print("\nroll a D12 to deflect!")
    input(">>> ")
    roll = sir(12)
    if dicerolle <= 8:
        print("The perpetrator dealt", damage,"Damage!")
        guh = damage - (damage * 2)
        hc(guh)
    else:
        print("You Deflected The Hit!")
        if health <= 0:
            ded()
            quit()
    time.sleep(2)

def attemptrun():
    global damage
    clsc()
    print("You Are Attempting To Run!")
    contimue()
    roll = sir(20)
    print("You Rolled",roll)
    if roll >= 15:
        print("You Managed To Excape Unharmed!")
    else:
        print("You Excaped But Got Caught On A Bush","\n-3 Health!")
        hc(-3)
        if health <= 0:
            ded()
            exit()

def fightseqzombie():
    global defence, mhealth, exp
    while True:
        clsc()
        print("enemy has", mhealth,"health currently")
        print("Rolling For Defence")
        roll = sir(20)
        print("Number:", roll)
        contimue()
        time.sleep(1)
        if roll >= defence:
                clsc()
                print("Your Attack Will Deal Damage","\n1: Attack (D5 + Player LvL)")
                imput = int(input(">>> "))
                if imput == 1:
                    roll = sir(5)
                    rolldmg = roll + playerlvl
                    print("you did",rolldmg,"damage!")
                    if rolldmg >= mhealth:
                        expm = random.randint(1, 3)
                        expm = expm * (1+(playerlvl*0.25))
                        print("you killed the enemy, you get", expm,"exp!")
                        arexp(expm)
                        lvlupcheck()
                        input("\nPress Enter To Go Back")
                        break
                    else:
                        hmissenc(rolldmg) 
        else:
            missenc()

def fightseqskeleton():
    global defence, mhealth, exp
    while True:
        clsc()
        print("enemy has", mhealth,"health currently")
        print("Rolling For Defence")
        roll = sir(20)
        print("Number:", roll)
        contimue()
        time.sleep(1)
        if roll >= defence:
                clsc()
                print("Your Attack Will Deal Damage","\n1: Attack (D5 + Player LvL)")
                imput = int(input(">>> "))
                if imput == 1:
                    roll = sir(5)
                    rolldmg = roll + playerlvl
                    print("you did",rolldmg,"damage!")
                    if rolldmg >= mhealth:
                        expm = random.randint(1, 25)
                        expm = expm / ((1+(playerlvl))/2)
                        print("you killed the enemy, you get", expm,"exp!")
                        exp = exp + expm
                        lvlupcheck()
                        input("\nPress Enter To Go Back")
                        break
                    else:
                        hmissenc(rolldmg) 
        else:
            missenc()

def encounter():
    global defence, health, mhealth, exp, enemylvl
    enemylvl = enclvl()
    wildcardcheck()
    enemytype = random.randint(1,2)
    if enemytype == 1:
        zombie(enemylvl)
        print("you have encountered a zombie!")
        print("1: Attack","\n2: Run")
        imput = int(input(">>>"))
        if imput == 1:
            fightseqzombie()
        if imput == 2:
            attemptrun()
    if enemytype == 2:
        skeleton(enemylvl)
        print("you have encountered a skeleton!","\n1: Attack","\n2: Run")
        imput = int(input(">>>"))
        if imput == 1:
            fightseqskeleton()
        if imput == 2:
            attemptrun()


### DiceRoll ### 
dicerolle = 0
dicerolls = []
def diceroll(sides,numof):
    for i in range(numof):
        dicerolls.append(random.randint(1, sides))
def sir(sides):
    dicerolle = random.randint(1, sides)
    dicerolls.append(dicerolle)
    return dicerolle

### QOL Stuff ###
def ded():
    print("You Died!")
    contimue()
def contimue():
    input("Press Any Key To Continue")
def hc(ammount):
    global health
    health = health + ammount
def hl():
    global health
    print(health)
def arexp(ammount):
    global exp
    exp = exp + ammount
def llist():
    global playerlvl
    playerlvl = playerlvl
    return playerlvl
##################            
            

def enclvl():
    global enemylvl, playerlvl
    if playerlvl == 0:
        enemylvl = random.randint(0, 0)
    elif playerlvl == 2:
        enemylvl == random.randint(0, 1)
    for i in range(2, 11):
        if playerlvl == i:
            lvlcap = i
            lvlbase = 0
            lvlbase = lvlcap - 2
            enemylvl = random.randint(lvlbase,lvlcap)
            #print("plvl:", playerlvl, "i = ", i, "lvlcap:", lvlcap)
    return enemylvl

### Player LvL Code Stuff ###
playerlvl = 0
exp = 0
lvlxpm = 10
def lvlupcheck():
    global exp, playerlvl, lvlxpm, health
    if playerlvl == 10:
        print("Max Level!","\n Overflow Exp:", exp)
    elif exp >= lvlxpm:
        playerlvl = playerlvl + 1
        lvlxpm = lvlxpm + lvlxpm
        health = health + 20
        exp = 0
        playstats()
    else:
        playstats()

def playstats():
    print("level:", playerlvl,"\namount of exp:", exp,"\nexp until next level:", lvlxpm)
    time.sleep(2)

### Trivia ###
#coming soon
lvl1tcomp = False
lvl2tcomp = False
lvl3tcomp = False
lvl4tcomp = False
lvl5tcomp = False
lvl6tcomp = False
lvl7tcomp = False
lvl8tcomp = False
lvl9tcomp = False
lvl10tcomp = False
