# connect the Turtle and random libraries (aka "modules")
import turtle, random

# let's make a turtle
tina = turtle.Turtle()
tina.speed(50)
# list of colors
colors = ["pink", "blue", "yellow", "green", "orange", "aqua"]


# random color picker
def color_tina():
    pick = random.randint(0, len(colors) - 1)
    tina.color(colors[pick])


def super_circles(size):
    for x in range(1, 11):
        color_tina()
        tina.circle(size * x)


def triangle(size):
    color_tina()
    tina.forward(size)
    tina.right(120)
    tina.forward(size)
    tina.right(120)
    tina.forward(size)


# let's make some methods, like plays in a playbook
def square(some_turtle):
    # stop writing
    some_turtle.penup()
    # go to the middle
    some_turtle.goto(0, 0)
    # start writing
    some_turtle.pendown()
    # go up
    some_turtle.goto(0, 50)
    # go right
    some_turtle.goto(50, 50)
    # go down
    some_turtle.goto(50, 0)
    # go back to the start
    some_turtle.goto(0, 0)


# let's make tina draw that square
# she'll fill in the spot of "some_turtle"
square(tina)

# let's draw a circle in the middle
tina.goto(25, 0)
tina.circle(25)

# call my fancy new functions
super_circles(10)

# AT THE END OF MY APP, I WILL USE A CONDITIONAL
# A conditional is another word for "if statement"
answer = input("?")
print("You just said: " + answer)
if True == True:
    print("The condition was True")
if answer == "Lebron":
    print("I Love Lebron")
elif answer == "circle":
    print("OH, I know that one!")
    circle(10)
elif answer == "move":
    tina.goto(random.randint(-200, 200), random.randint)
else:
    print("That is not in my commands.")

import turtle

turtle.pendown()
for i in range(8):
    turtle.forward(100)
    turtle.right(360 / 8)

turtle.penup()
turtle.goto(20, -20)
turtle.pendown()

for i in range(8):
    turtle.forward(40)
    turtle.right(360 / 8)

import turtle

spiral = turtle.Turtle()

for i in range(20):
    spiral.forward(i * 10)
    spiral.right(144)

turtle.done()

import turtle

painter = turtle.Turtle()

painter.pencolor("aqua")

for i in range(50):
    painter.forward(50)
    painter.left(123)  # Let's go counterclockwise this time

painter.pencolor("purple")
for i in range(50):
    painter.forward(100)
    painter.left(123)

turtle.done()

