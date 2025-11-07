import turtle
from random import *
bob = turtle.Turtle()

def square(size):
    for times in range(4):
        bob.forward(size)
        bob.left(90)

def triangle(size):
    for times in range(3):
        bob.forward(size)
        bob.left(120)

def pentagon(size):
    for times in range(5):
        bob.forward(size)
        bob.left(72)

def polygon(size, side, c):
    angle = 360 / side
    bob.color(c)
    for times in range(side):
        bob.forward(size)
        bob.left(angle)
# normal polygon

def polygonfill(size, side, c):
    angle = 360 / side
    bob.color(c)
    bob.begin_fill()
    for times in range(side):
        bob.forward(size)
        bob.left(angle)
    bob.end_fill()
# filled in polygon

def comet(size, angle, length):
    for times in range(length):
        bob.forward(size)
        bob.left(angle)
        bob.width(times)
# draws a comet-like shape

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
# teleports bob easily

def stair(distance, amount, c, w):
    bob.color(c)
    bob.width(w)
    for times in range(amount):
        bob.forward(distance)
        bob.left(90)
        bob.forward(distance)
        bob.right(90)
# draws a staircase

def drawSquare(sizeS, sizeC):
    for times in range(4):
        bob.forward(sizeS)
        bob.right(90)
        bob.circle(sizeC)
# draws a square with circles on each corner

def tree(x,y):
    jump(x,y)
    polygonfill(100, 3, "green")
    bob.forward(38)
    bob.right(90)
    polygonfill(25, 4, "brown")
    bob.left(90)
# draws a tree

def flower(x,y):
    jump(x,y)
    for times in range(5):
        polygonfill(50, 3, "light pink")
        bob.right(72)
    bob.left(36)
    bob.forward(5)
    bob.color("yellow")
    bob.begin_fill()
    bob.circle(10)
    bob.end_fill()

def rose(size):
    for times in range(200):
     bob.circle(size*2)
     bob.forward(times*2)
     bob.left(91)

def loop(size):
    for times in range(256):
        c = (0, 0, times)
        bob.color(c)
        bob.circle(50)
        bob.forward(size * 2)
        bob.left(90)

def f(size):
    for times in range(256):
        bob.width(10)
        c = (255, times, 100)
        bob.color(c)
        bob.circle(size)
        bob.forward(times * 2)
        bob.left(90)

