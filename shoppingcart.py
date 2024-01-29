
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

name = input("What is your name")
print("Hello " + name)

num_of_apples = input("How many apples: ")
cost = num_of_apples*apple

print(message + cost)

