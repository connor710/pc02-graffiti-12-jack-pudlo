#!/usr/bin/env python
# coding: utf-8
'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Jack Pudlo
Sep 4, 2020
'''

from turtle import *

colormode(255)

panel = Screen()
w = 750
h = 750
panel.setup(width=w, height=h)

panel.bgcolor("lightsteelblue1")
panel.bgpic("Bezos.gif")

speed(10)
color('black')
pensize(20)

#Black bars on either side of jeff
up()
goto(-150, 750)
down()
right(90)
forward(1500)
up()

goto(150, 750)
down()
forward(1500)
up()

#pink glasses
goto(-40, 112)
pensize(8)
down()
color('pink')
circle(20)
up()

goto(28, 120)
pensize(6)
down()
circle(17)
up()

left(90)
setheading(188)
pensize(5)
down()
forward(30)
up()

goto(-40, 112)
setheading(180)
pensize(3)
down()
forward(54)
up()

# l is set to 10 the length of the sides of square 
l = 10
#added a set to 90 for the angle of the square
a = 90

color('orange')
fillcolor('orange')
pensize(4)
goto(-85, 25)
down()
setheading(270)
begin_fill()
forward(l)
right(a)
forward(l)
right(a)
forward(l)
right(a)
forward(l)
up()
end_fill()

color('red')
fillcolor('red')
forward(35)
right(a)
forward(40)
down()
setheading(270)
begin_fill()
forward(l)
right(a)
forward(l)
right(a)
forward(l)
right(a)
forward(l)
up()
end_fill()

color('teal')
fillcolor('teal')
forward(35)
right(a)
forward(40)
down()
setheading(270)
begin_fill()
forward(l)
right(a)
forward(l)
right(a)
forward(l)
right(a)
forward(l)
up()
end_fill()

color('purple')
fillcolor('purple')
forward(40)
left(a)
forward(10)
down()
setheading(270)
begin_fill()
forward(l)
right(a)
forward(l)
right(a)
forward(l)
right(a)
forward(l)
up()
end_fill()

color('skyblue')
fillcolor('skyblue')
forward(25)
left(a)
forward(40)
down()
setheading(270)
begin_fill()
forward(l)
right(a)
forward(l)
right(a)
forward(l)
right(a)
forward(l)
up()
end_fill()

goto(-78, 55)
pensize(2)
color('gold')
down()
fillcolor('skyblue')
begin_fill()
forward(5)
right(a)
forward(5)
right(a)
forward(5)
right(a)
forward(5)
right(a)
up()
end_fill()
