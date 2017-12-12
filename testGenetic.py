from personneClass import Personne
import random

boss = Personne(5000,25,25,0)
bestFighters = []
for i in range (10):
    bestFighters.append(Personne(0,0,0,0))

def fight(boss, personnage):
    while (boss.currentHP and personnage.currentHP) > 0:
        boss.currentHP -= (personnage.attaque * (boss.defense/100))
        personnage.currentHP -= (boss.attaque * (personnage.defense/100)) 

def saveFighter(personnage):
    j = 0
    while j < 10:
        if (bestFighters[j].value == 0):
            bestFighters[j] = personnage
            break
        elif (bestFighters[j].value < personnage.value and j != 9):
            bestFighters.insert(j, personnage)
            bestFighters.pop()
            break
        j+=1

def initFirstGen():
    listPersonnage = []
    for i in range(1000):
        hp = random.randint(20,30)
        atk = random.randint(7,11)
        deff = random.randint(40,50)
        listPersonnage.append(Personne(hp,atk,deff,1))
        fight(boss, listPersonnage[i])
        listPersonnage[i].value = round(5000 - boss.currentHP)
        saveFighter(listPersonnage[i])
        boss.currentHP = 5000
    for i in range(10):
        print("Fighter : point de vie ", bestFighters[i].hp,
              " - attaque ", bestFighters[i].attaque,
              " - defense ", bestFighters[i].defense,
              " - value ", bestFighters[i].value,
              " - generation ", bestFighters[i].generation)
    print("--All the fights of the generation 1 are over--")

def nextGen(generation):
    listPersonnage = []
    oldFighters = list(bestFighters)
    for i in range (10000):
        selectedFighterBreeder = random.randint(0,4)
        coefList = []
        for j in range (3):
            coefList.append(round(random.uniform(0.95,1.05),2))
        listPersonnage.append(Personne(round(oldFighters[selectedFighterBreeder].hp*coefList[0]),
                                     round(oldFighters[selectedFighterBreeder].attaque*coefList[1]),
                                     round(oldFighters[selectedFighterBreeder].defense*coefList[2]),
                                     generation))
        fight(boss, listPersonnage[i])
        listPersonnage[i].value = round(5000 - boss.currentHP)
        saveFighter(listPersonnage[i])
        boss.currentHP = 5000
    for i in range(10):
        print("Fighter : point de vie ", bestFighters[i].hp,
              " - attaque ", bestFighters[i].attaque,
              " - defense ", bestFighters[i].defense,
              " - value ", bestFighters[i].value,
              " - generation ", bestFighters[i].generation)
    print("--All the fights of the generation ", generation, " are over--")


initFirstGen()
currentGen = 2
while currentGen < 21:
    nextGen(currentGen)
    currentGen+=1
