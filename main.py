from turtle import Turtle, Screen
import threading

def draw(turtle, start, stop, step):
    for x in range(start, stop + 1, step):
        for y in range(start, stop + 1, step):
            turtle.goto(x * 20, y * 20)
            turtle.stamp()



redB = Turtle(shape="square")
redB.shapesize(8)
redB.color("red")
redB.penup()
draw(redB, -12, 12, 12)




yellowB = Turtle(shape="square")
yellowB.shapesize(4)
yellowB.color("gold")
yellowB.penup()
draw(yellowB, -6, 6, 12)




screen = Screen()
screen.exitonclick()
