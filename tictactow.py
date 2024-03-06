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

        # 0, 1, 2
grid = [['_','_','_'], #0
        ['_','_','_'], #1
        ['_','_','_']] #2

#draw a square
def square(length, column, row):
    turtle_object.goto(startx+column*100, starty+ row*-100)
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
    turtle_object.goto(startx+column*100 + 10, starty+ row*-100 -10)

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
    turtle_object.goto(startx+column*100 + 80, starty+ row*-100 - 80)

    turtle_object.pendown()
    turtle_object.pencolor("green")
    turtle_object.pensize(5)
    turtle_object.circle(radius)
    turtle_object.penup()

def draw_grid():
    for row in range(3):
        for column in range(3):
            square(100,column,row)
    return

draw_grid()

whoseturn = 1
turn = input("Please say which column and row, separate with a space (1-3): ")
turn = turn.split(" ") #turn is ["column","row"]
column = int(turn[0]) - 1
row = int(turn[1]) - 1

grid[column][row] = whoseturn
print(grid)

if whoseturn == 1:
    cross(100, column, row)
    whoseturn = 2
elif whoseturn == 2:
    circle(80, column, row)
    whoseturn = 1

input()

