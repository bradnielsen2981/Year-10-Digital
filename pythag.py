# A FUNCTION is a piece of code that serves a purpose
# A function is defined by the NAME and round brackets ()
# Some functions have INPUTs and give OUTPUTs
import math
y = 1000

def find_hypotenuse(a, b):
    print(y)
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

print(c)