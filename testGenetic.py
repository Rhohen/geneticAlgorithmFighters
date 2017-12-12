from personneClass import Personne
import random

boss = Personne(500,50,50,0)
bestFighters = []
for i in range (5):
    bestFighters.append(Personne(0,0,0,0))

def fight(boss, personnage):
    while (boss.currentHP and personnage.currentHP) > 0:
        boss.currentHP -= personnage.attaque * (boss.defense / 100)
        personnage.currentHP -= boss.attaque * (personnage.defense / 100)  
    print("boss : ",boss.hp, " personnage : ", personnage.currentHP)

def saveFighter(personnage):
    j = 0
    while j < 5:
        if (bestFighters[j].value == 0):
            bestFighters[j] = personnage
            break
        elif (bestFighters[j].value < personnage.value and j != 4):
            bestFighters.insert(j, personnage)
            bestFighters.pop()
            break
        j+=1

def initFirstGen():
    i = 0
    listPersonnage = []
    while i < 100:
        listPersonnage.append(i)
        hp = random.randint(80,120)
        atk = random.randint(5,15)
        deff = random.randint(5,15)
        listPersonnage[i] = Personne(hp,atk,deff, 1)
        print("personnage ", i, " :  point de vie ", listPersonnage[i].hp, " - attaque ", listPersonnage[i].attaque, " - defense ", listPersonnage[i].defense)
        fight(boss, listPersonnage[i])
        listPersonnage[i].value = round(500 - boss.currentHP)
        print(listPersonnage[i].value)
        saveFighter(listPersonnage[i])
        boss.currentHP = 500
        i+=1
    for i in range(5):
        print("Fighter : point de vie ", bestFighters[i].hp, " - attaque ", bestFighters[i].attaque, " - defense ", bestFighters[i].defense, " - value ", bestFighters[i].value)

def nextGen(generation):
    i = generation
    
initFirstGen()

