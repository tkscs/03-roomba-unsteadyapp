# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed, up, down, goto
import room
def in_circle(x, y, radius, center):
    # equation of a circle:
    # (x – x1)² + (y – y1)²= r²
    x1 = center[0]
    x2 = center[1]
    return (x - x1)**2 + (y - x2)**2 <= radius**2
def drawRadius(radius):
    shapes = []
    alcove_radius = radius // 2
    n_rows = (radius*2 + 1)*4
    n_cols = (radius*2 + 1)*4

    for col in range(n_cols):
        start_x = 40 * col
        end_x = 40 * (col + 1)
        center = (radius + alcove_radius*2,radius + alcove_radius*2)
        for row in range(n_rows):
            if in_circle(col, row, radius, center):
                start_y = 40 * row
                end_y = 40 * (row + 1)
                shape = [(start_x, start_y), (end_x, end_y)]
                shapes=shapes+shape
    return(shapes)
toDraw = drawRadius(5)
print(toDraw)
if(True):
    An_alcoves = 1
    Aradius = 5
    # Make the turtle go faster
    speed(20)
    # Draw the Level 4 version of the room
    window = room.draw_room(level = 4, n_alcoves = 1,radius=5)
    ###
    # Start your code here
    bump = False
    toDraw.pop(0)
    for i in toDraw:
        if(False):
            if(bump):
                bump = False
                down()
            else:
                bump = True
                up()
        goto(i[0],i[1])
        #goto(i[1][0],i[1][1])


        

    
    
    # End your code here
    ###
    
    window.exitonclick()