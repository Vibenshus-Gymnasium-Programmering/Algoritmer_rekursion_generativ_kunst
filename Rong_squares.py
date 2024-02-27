import numpy as np
import turtle

fill_posibility = [0, 10, 30, 40, 101, 101]
shapearray1 = np.arange(4).reshape(2, 2)
shapearray2 = np.arange(9).reshape(3, 3)


def fill_square(x, y, width):
    t.fillcolor(
        np.random.randint(50, 100),
        np.random.randint(0, 100),
        np.random.randint(150, 255),
    )
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(width)
        t.left(90)
    t.end_fill()
    t.penup()


def plot_squares(width, level, x, y, N):
    if level < N:
        fill = np.random.randint(0, 99) < fill_posibility[level]
        if fill:
            fill_square(x, y, width)
        else:
            # chooseshape = np.random.randint(1, 100) < 80
            chooseshape = True
            if chooseshape:
                for (i, j), _ in np.ndenumerate(shapearray1):
                    plot_squares(
                        width / 2, level + 1, x + i * width / 2, y + j * width / 2, N
                    )
            else:
                for (i, j), _ in np.ndenumerate(shapearray2):
                    plot_squares(
                        width / 3, level + 1, x + i * width / 3, y + j * width / 3, N
                    )


t = turtle.Turtle()
# t.hideturtle()
t.speed(0)
turtle.colormode(255)
s = turtle.Screen()
s.setup(600, 600)
t.pencolor("white")
t.penup()
t.width(2)
t.goto(-200, -200)
plot_squares(500, 0, -200, -200, 5)
turtle.done()
