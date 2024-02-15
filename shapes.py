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

for a in range(0,720,10):
    square(a/2)
    turtle_object.right(10)
    turtle_object.color(255-int(a/5),0,0)


input("Press enter to continue")




