key = False
death = False
import random
gold = 0

answer = input("You are travelling along a road and come across a rock. 1. Pick up the rock. 2. Kick the rock. 3. Continue on" )
answer = int(answer) #change it to an integer

if answer == 1:
    print("Under the rock, you find a key.")
    if True:
        key = True
elif answer == 2: 
    print("You kick the rock, it hits a dragon. He burns you. You dead!")
    death = True    
else:
    print("You whistle a tune.")

if death == False:
    answer = input("You come across a giant. He asks you how tall you think he is: ")
    answer = int(answer)
    if answer < 10:
        print("The giant gets angry and steps on you. You dead")
        death = True
    elif answer < 100:
        print("You run through the giants legs and come to a door.")
        if key:
            print("You get through the door. You lived!")   
        else:
            print("You are squashed. You dead")
            death = True
    else:
        print("The giant smiles but kills you anyway. You dead!")

if death == False:
    input("You find yourself in a dungeon with a dragon. Roll 4-6 to live:")
    roll = random.randint(1,6)
    if roll >= 4:
        print("You dodge to the side. Steal some jewels and run away.")
        gold = 1000
    else:
        print("The dragons laughs and breaths fire. You dead!")





