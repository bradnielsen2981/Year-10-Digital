# A FUNCTION is a piece of code that serves a purpose
# A function is defined by the NAME and round brackets ()
# Some functions have INPUTs and give OUTPUTs
import math
import mylib

y = 1000 #A global variable is defined outside any block of code and is available anywhere. 
print(mylib.y)

def find_hypotenuse(a, b):
    csquared = a*a + b*b
    c = math.sqrt(csquared)
    return c
# A block of code is defined by a colon : and an indent. Once you break the indent, the block of code has ended
# Variables inside a block of code are local variables. Once the block is exited, the variable is destroyed. (Garbage Collection). Variable Scope
# Variables inside a function are referred to as local variables 
e = float(input("Please enter side A"))
f = float(input("Please enter side B"))
hyp = find_hypotenuse(e,f)
print("The hyptenuse is:" + str(hyp))


#STUDENT ACTIVITY

#WRITE A FUNCTION
def hero_name

#ACTION HERO NAME: (first name of a main character in the last movie you watched, last food you ate)
#CRIMINAL NAME: (name of your favorite perfume/cologne, favorite candy bar)
#DETECTIVE NAME:(favorite color, favorite animal)

#WRITE A FUNCTION THAT WILL CALCULATE THE AREA OF A CIRCLE 
def area_circle

