print("\033c")
#player 1 places an X
#player 2 places a 0
#logic to determine the winner (three in a row, horizontal, vertical, diagonal)

#draw board
import turtle
turtle.bgcolor("black")
turtle_object = turtle.Turtle()
turtle_object.speed(0)
startx = -150
starty = 150
turtle_object.goto(startx,starty)

#draw a square
def square(length, column, row):
    turtle_object.goto(startx + column*100, starty+row*100)

    turtle_object.pensize(1)
    turtle_object.pencolor("white")
    turtle_object.pendown()
    for side in range(4):
        turtle_object.forward(length)
        turtle_object.right(90)
    turtle_object.penup()
    return

#draw a cross
def cross(length, column, row):
    turtle_object.goto(startx + column*100, starty+row*100)

    turtle_object.pendown()
    turtle_object.pensize(5)
    turtle_object.pencolor("red")
    turtle_object.right(45)
    turtle_object.forward(length)
    turtle_object.penup()
    turtle_object.left(180)
    turtle_object.forward(length/2)
    turtle_object.left(90)
    turtle_object.forward(length/2)
    turtle_object.pendown()
    turtle_object.left(180)
    turtle_object.forward(length)
    turtle_object.penup()
    return

#draw a circle
def circle(radius, column, row):
    turtle_object.goto(startx + column*100, starty+row*100)

    turtle_object.pendown()
    turtle_object.pencolor("green")
    turtle_object.pensize(5)
    turtle_object.circle(radius)
    turtle_object.penup()

def draw_grid():
    for row in range(3):
        for cell in range(3):
            square(100)
            turtle_object.forward(100)
        turtle_object.right(180)
        turtle_object.forward(300)
        turtle_object.right(180)
        turtle_object.right(90)
        turtle_object.forward(100)
        turtle_object.left(90)
    return

#draw_grid()
cross(100,1,1)

input()

