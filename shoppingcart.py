print("hello world")

#EACH VARIABLE HAS A DATATYPE
money = 50 #integer
apple = 1.5 #float
num_of_apples = 20 #integer
message = "Cost is equal: " #string 
out_of_money = False #Boolean (yes or no) 0, or 1

print(type(money))
print(type(apple))
print(type(num_of_apples))
print(type(message))
print(type(out_of_money))

#VARIABLES ARE STORED IN MEMORY
#NAME error - means you referred to a variable that does not exit

name = input("What is your name: ")
print(type(name))
print("Hello " + (name*10))

#TYPE error - means you referred to a variable by the wrong type

num_of_apples = input("How many apples: ")
cost = int(num_of_apples)*apple
print(message + str(cost))


# A FUNCTION is a piece of code that serves a purpose
# A function is defined by the NAME and round brackets ()
# Some functions have INPUTs and give OUTPUTs

import math

def find_hypotenuse(a, b):
    csquared = a*a + b*b
    c = math.sqrt(csquared)
    return c

a = input("Please enter side A")
b = input("Please enter side B")
hyp = find_hypotenuse(a,b)
