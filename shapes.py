import turtle
import random
turtle.bgcolor("black")
turtle_object = turtle.Turtle()
turtle_object.goto(0,0)
turtle_object.speed(100)

def square(length):
    for i in range(4):
        turtle_object.forward(length)
        turtle_object.right(90)
    return

def shape(length, num_sides, colour, vec):
    global turtle_object
    turtle_object.goto(vec)
    turtle_object.pencolor("white")
    turtle_object.pendown()
    turtle_object.fillcolor(colour)
    turtle_object.begin_fill()
    angle = int(360/num_sides)
    for s in range(num_sides):
        turtle_object.forward(length)
        turtle_object.right(angle)
    turtle_object.end_fill()
    turtle_object.penup()
    return

shape(20, 7, "red", (0,0))


colourlist = ['red','blue','green','purple','yellow','orange']

#special for loop where loop through values inside a list
for colour in colourlist:
    x = random.randint(-400,400)
    y = random.randint(-300,300)
    vec = (x,y)
    shape(50, 4, colour, vec)












'''
for a in range(0,720,10):
    square(a/2)
    turtle_object.right(10)
    turtle_object.color(255-int(a/5),0,0)
'''

input("Press enter to continue")




