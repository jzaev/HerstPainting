from turtle import Turtle, Screen
from random import choice

color_table = [(253, 251, 246),
               (244, 251, 247),
               (206, 159, 112),
               (252, 247, 249),
               (226, 237, 244),
               (222, 206, 120),
               (138, 173, 192),
               (44, 106, 137),
               (138, 183, 149),
               (15, 52, 75)]

my_turtle = Turtle()
my_turtle.shape("circle")
screen = Screen()
screen.colormode(255)
my_turtle.pu()

for i in range(0, 10):
    my_turtle.sety(i * 30)
    my_turtle.setx(0)
    for j in range(0, 10):
        my_turtle.color(choice(color_table))
        my_turtle.stamp()
        my_turtle.setx(j * 30)

my_turtle.color((255, 255, 255))


screen.exitonclick()
