# A FUNCTION is a piece of code that serves a purpose
# A function is defined by the NAME and round brackets ()
# Some functions have INPUTs and give OUTPUTs

import math

def find_hypotenuse(a, b):
    csquared = a*a + b*b
    c = math.sqrt(csquared)
    return c

a = float(input("Please enter side A"))
b = float(input("Please enter side B"))
hyp = find_hypotenuse(a,b)

print("The hyptenuse is:" + str(hyp))