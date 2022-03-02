from time import sleep

import turtle

#a = turtle.Screen()
#x = turtle.Turtle()
#x.hideturtle()
#x.penup()
#x.color("grey")
#x.goto(-100, 0)
#for p in range(0, 3):
  #  x.fillcolor("blue")
   # x.begin_fill()
    #x.goto(50 * p, 100)
    #x.pendown()
    #x.width(5)
    #for i in range(0, 4):
     #   x.forward(50)
      #  x.right(90)

    #x.end_fill()
    #x.penup()

#for p in range(0, 3):
 #   x.fillcolor("red")

  #  x.begin_fill()
   # x.goto(50 * p, 50)
    #x.pendown()
    #x.width(5)
    #for i in range(0, 4):
     #   x.forward(50)
      #  x.right(90)

    #x.end_fill()
    #x.penup()

#for p in range(0, 3):
 #   x.fillcolor("yellow")
  #  x.begin_fill()
   # x.goto(50 * p, 0)
    #x.pendown()
    #x.width(5)
    #for i in range(0, 4):
     #   x.forward(50)
      #  x.right(90)

    #x.end_fill()
    #x.penup()

# cube = np.ones((3, 3, 3), dtype='bool')
# print(cube)

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.set_facecolor('White')
# ax.voxels(cube, facecolors="Blue")
# ax.axis('off')
# plt.show()
#x.goto(-100, -100)
#style = ('Courier', 30, 'italic')
#x.write("Next Move: Koi bi!!", font=style, align='center')
#sleep(500)
#print("Hello")
from array import *


class State:

    sideup = [[2, 4, 2], [6, 1, 1], [1, 4, 3]]
    sidedown = [[5, 2, 5], [6, 3, 1], [2, 4, 6]]
    sideleft = [[4, 4, 2], [1, 4, 3], [4, 5, 6]]
    sideright = [[6, 6, 3], [2, 5, 3], [6, 2, 1]]
    sidefront = [[5, 2, 4], [5, 2, 5], [3, 3, 1]]
    sideback = [[5, 3, 1], [6, 6, 5], [4, 1, 3]]
    def __init__(self):

        self.sideup = [[2, 4, 2], [6, 1, 1], [1, 4, 3]]
        self.sidedown = [[5, 2, 5], [6, 3, 1], [2, 4, 6]]
        self.sideleft = [[4, 4, 2], [1, 4, 3], [4, 5, 6]]
        self.sideright = [[6, 6, 3], [2, 5, 3], [6, 2, 1]]
        self.sidefront = [[5, 2, 4], [5, 2, 5], [3, 3, 1]]
        self.sideback = [[5, 3, 1], [6, 6, 5], [4, 1, 3]]

    # white=1    , blue=2      ,yellow=3      ,red=4     ,orange=5       ,green=6
    def print_(self):
        print("Front: ")
        for r in self.sidefront:
            for c in r:
                print(c, end=" ")
            print()
        print("Left: ")

        for r in self.sideleft:
            for c in r:
                print(c, end=" ")
            print()
        print("Right: ")

        for r in self.sideright:
            for c in r:
                print(c, end=" ")
            print()
        print("Up: ")

        for r in self.sideup:
            for c in r:
                print(c, end=" ")
            print()
        print("Down: ")

        for r in self.sidedown:
            for c in r:
                print(c, end=" ")
            print()
        print("Back: ")

        for r in self.sideback:
            for c in r:
                print(c, end=" ")
            print()

    def move_down_left(self):

        var1 = self.sidefront[0][0]
        var2 = self.sidefront[1][0]
        var3 = self.sidefront[2][0]

        self.sidedown[0][0], var1 = var1, self.sidedown[0][0]
        self.sidedown[1][0], var2 = var2, self.sidedown[1][0]
        self.sidedown[2][0], var3 = var3, self.sidedown[2][0]

        self.sideback[0][0], var1 = var1, self.sideback[0][0]
        self.sideback[1][0], var2 = var2, self.sideback[1][0]
        self.sideback[2][0], var3 = var3, self.sideback[2][0]

        self.sideup[0][0], var1 = var1, self.sideup[0][0]
        self.sideup[1][0], var2 = var2, self.sideup[1][0]
        self.sideup[2][0], var3 = var3, self.sideup[2][0]

        self.sidefront[0][0], var1 = var1, self.sidefront[0][0]
        self.sidefront[1][0], var2 = var2, self.sidefront[1][0]
        self.sidefront[2][0], var3 = var3, self.sidefront[2][0]

        var1 = self.sideleft[0][0];
        var2 = self.sideleft[0][1];
        var3 = self.sideleft[0][2];

        self.sideleft[0][2], var1 = var1, self.sideleft[0][2];
        self.sideleft[1][2], var2 = var2, self.sideleft[1][2];
        self.sideleft[2][2], var3 = var3, self.sideleft[2][2];

        self.sideleft[2][2], var1 = var1, self.sideleft[2][2];
        self.sideleft[2][1], var2 = var2, self.sideleft[2][1];
        self.sideleft[2][0], var3 = var3, self.sideleft[2][0];

        self.sideleft[2][0], var1 = var1, self.sideleft[2][0];
        self.sideleft[1][0], var2 = var2, self.sideleft[1][0];
        self.sideleft[0][0], var3 = var3, self.sideleft[0][0];

        self.sideleft[0][2], var1 = var1, self.sideleft[0][2];
        self.sideleft[0][1], var2 = var2, self.sideleft[0][1];
        self.sideleft[0][0], var3 = var3, self.sideleft[0][0];


state1 = State()
state1.print_()
state1.move_down_left()
state1.print_()