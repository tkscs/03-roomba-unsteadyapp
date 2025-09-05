# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Aron <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(20)

# Draw the Level 3 version of the room
window = room.draw_room(level = 3,radius=5)

###
# Start your code here
forward(40)
right(90)
forward(40*3)
left(90)
def f(x):
    forward(40*x)
for i in range(0,3):
    f(8)
    left(90)
    f(1)
    left(90)
    f(8)
    right(90)
    f(1)
    right(90)
f(8)
right(90)
f(3)
left(90)
f(1)
left(180)
f(10)
left(180)
f(1)
left(90)
f(3)
#edge
right(90)
f(1)
left(90)
f(1)
right(90)
f(6)
right(90)
f(8)
right(90)
f(6)
left(180)
f(3)
right(90)
f(1)
right(180)
f(10)
# End your code here
###
 
window.exitonclick()