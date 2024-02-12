key = False
death = False

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
    
    


