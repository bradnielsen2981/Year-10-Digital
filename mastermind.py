
#second player then also chooses 4 colours from (red,yellow,blue,green,black,white)
#second player is then told how many were in the correct order, and how many were correct but in the wrong position
#second player then repeats the process.
#second player has only 7 lives

#first player chooses 4 colours
code = input("Choose 4 colours from red,green,blue,yellow,black and white. (Type them in a sequence separated by a space): ")
code = code.split(" ")
# check that the code consists of 4 colours

#second player choose 4 colours
playercode = input("Choose 4 colours from red,green,blue,yellow,black and white. (Type them in a sequence separated by a space): ")
playercode = playercode.split(" ")

for colour in code:
    print(colour)