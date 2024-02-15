import turtle

turtle.colormode(255)
turtle.bgcolor("black")
turtle_object = turtle.Turtle()

turtle_object.goto(0,0)
turtle_object.pendown()
turtle_object.color("red")
turtle_object.speed(100)

def square(length):
    for i in range(4):
        turtle_object.forward(length)
        turtle_object.right(90)
    return

#create a function that will take the number of sides
#length of each side,
#colour
#draw the shape
#turtle_object.fillcolor()
#turtle_object.begin_fill()
#turtle_object.end_fill()
def shape(length, num_sides, colour, vec):
    turtle_object.goto(vec)
    turtle_object.fillcolor = colour
    turtle_object.begin_fill()
    angle = int(360/num_sides)
    for s in range(num_sides):
        turtle_object.forward(length)
        turtle_object.right(angle)
    turtle_object.end_fill()

shape(20, 7, "red", (0,0))











'''
for a in range(0,720,10):
    square(a/2)
    turtle_object.right(10)
    turtle_object.color(255-int(a/5),0,0)
'''

input("Press enter to continue")




