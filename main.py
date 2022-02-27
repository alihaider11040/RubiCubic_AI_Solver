from time import sleep

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import turtle

a = turtle.Screen()
x = turtle.Turtle()
x.hideturtle()
x.penup()
x.color("grey")
x.goto(-100,0)
for p in range(0, 3):
    x.fillcolor("blue")
    x.begin_fill()
    x.goto(50*p, 100)
    x.pendown()
    x.width(5)
    for i in range(0,4):
        x.forward(50)
        x.right(90)

    x.end_fill()
    x.penup()

for p in range(0, 3):
    x.fillcolor("red")

    x.begin_fill()
    x.goto(50*p, 50)
    x.pendown()
    x.width(5)
    for i in range(0,4):
        x.forward(50)
        x.right(90)

    x.end_fill()
    x.penup()

for p in range(0, 3):
    x.fillcolor("yellow")
    x.begin_fill()
    x.goto(50*p, 0)
    x.pendown()
    x.width(5)
    for i in range(0,4):
        x.forward(50)
        x.right(90)

    x.end_fill()
    x.penup()

# cube = np.ones((3, 3, 3), dtype='bool')
# print(cube)

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.set_facecolor('White')
# ax.voxels(cube, facecolors="Blue")
# ax.axis('off')
# plt.show()
x.goto(-100, -100)
style= ('Courier', 30, 'italic')
x.write("Next Move: Koi bi!!", font=style, align='center')
sleep(500)
print("Hello")
