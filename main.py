from turtle import Turtle, Screen
import threading

def draw(turtle, start, stop, step):
    for x in range(start, stop + 1, step):
        for y in range(start, stop + 1, step):
            turtle.goto(x * 20, y * 20)
            turtle.stamp()

def redboxes(lock):
    lock.acquire()
    redB = Turtle(shape="square")
    redB.shapesize(8)
    redB.color("red")
    redB.penup()
    draw(redB, -12, 12, 12)
    lock.release()

def yellowboxes(lock):
    lock.acquire()
    yellowB = Turtle(shape="square")
    yellowB.shapesize(4)
    yellowB.color("gold")
    yellowB.penup()
    draw(yellowB, -6, 6, 12)
    lock.release()

lock = threading.Lock()

thread1 = threading.Thread(target=redboxes, args=(lock,))
thread2 = threading.Thread(target=yellowboxes, args=(lock,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

screen = Screen()
screen.exitonclick()
